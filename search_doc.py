import argparse
import os
import glob
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from util.lang_detect import is_meaning_str
from util.count_token import clean_html_txt, complete_html, contain_alpha_num
from text_match import text_correct  # call LLM here.
import json


def render_blk(block_html):
    mini_soup = BeautifulSoup(block_html, "html.parser")
    return mini_soup.get_text()


def extract_elements(soup):
    body = soup.find("body")
    if not body:
        return []

    def is_target_element(tag):
        if tag.name in [
            "p",
            "span",
            "li",
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "td",
            "th",
            "caption",
            "pre",
            "dl",
        ]:
            return True
        if tag.name == "a" and tag.parent == body:
            return True
        if tag.name == 'div':
            # Check if div contains only text nodes
            return all(isinstance(child, str) and child.strip() 
                       for child in tag.contents 
                       if child is not None)
        return False

    return body.find_all(is_target_element, recursive=True)


def search_html_files(directory, query, threshold=60, block_size=5):
    # List all HTML files in the directory
    html_files = [
        f for f in os.listdir(directory) if f.endswith((".html", ".xhtml", ".htm"))
    ]

    matching_files = []

    for html_file in html_files:
        curr_blk_size = block_size
        with open(os.path.join(directory, html_file), "r", encoding="utf-8") as file:
            content = clean_html_txt(file.read())

        soup = BeautifulSoup(content, "html.parser")
        paragraphs = extract_elements(soup)

        # Store the matched blocks with their scores and HTML
        matched_blks = []

        num_paragraphs = len(paragraphs)
        if num_paragraphs < curr_blk_size:
            curr_blk_size = num_paragraphs
        for i in range(num_paragraphs - curr_blk_size + 1):
            block = paragraphs[i : i + curr_blk_size]
            block_text = " ".join(paragraph.get_text() for paragraph in block)
            score = fuzz.partial_ratio(query.lower(), block_text.lower())
            if score >= threshold:
                # Find positions of start & end of the block in original HTML
                start_pos = content.find(str(block[0]))
                end_pos = content.find(str(block[-1])) + len(str(block[-1]))
                block_html = content[start_pos:end_pos]
                blk_html_txt = render_blk(block_html)
                val_score = fuzz.partial_ratio(query.lower(), blk_html_txt.lower())

                # Validate the block content contains matched query
                if  val_score >= threshold:
                    matched_blks.append((block_html, val_score))

        if matched_blks:
            # Calculate the average score for the document
            avg_score = sum(score for _, score in matched_blks) / len(matched_blks)
            matching_files.append((html_file, avg_score, matched_blks))

    # Sort matched files by their avg score in descending order
    matching_files.sort(key=lambda x: x[1], reverse=True)

    return matching_files


def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        # Skip the first element (meta info)
        return data[1:]
    except json.JSONDecodeError:
        print(f"Error: '{file_path}' is not a valid JSON")
        return None


def main():
    parser = argparse.ArgumentParser(description="Search a folder ")
    parser.add_argument("source", help="dir to load all ref html files")
    parser.add_argument("json_dir", help="dir to load input json files")
    parser.add_argument("-o", help="where to save json files of a book")
    parser.add_argument("-m", default="gpt3", help="model to correct text")

    args = parser.parse_args()

    json_paths = glob.glob(os.path.join(args.json_dir, "*.json"))

    for in_js_path in json_paths:
        # each js_path is 1 json file.
        js_basename = os.path.basename(in_js_path)
        para_list = load_json(in_js_path)

        for para in para_list:
            para_text = para["content"]
            if not is_meaning_str(para_text):
                if not contain_alpha_num(para_text) and len(para_text) < 5:
                    para["status"] = "invalid"
                else:
                    para["status"] = "skip"
                continue

            match_files = search_html_files(args.source, para_text)

            if match_files:
                # highest sim score file is used to search
                _, _, blocks0 = match_files[0]
                block_html, _ = next(iter(blocks0[1:]), blocks0[0])

                simple_html = complete_html(block_html)
                correct_para = text_correct(simple_html, para_text, args.m)

                if correct_para:
                    para["content-fix"] = correct_para
                    para["status"] = "corrected"
                else:
                    para["status"] = "try_again"

                files, scores, _ = zip(*match_files)
                para["search-doc"] = files
                para["search-score"] = scores

            else:
                para["status"] = "not_found"

        if not os.path.exists(args.o):
            os.makedirs(args.o)

        save_target = os.path.join(args.o, js_basename)
        with open(save_target, "w", encoding="utf-8") as file:
            json.dump(para_list, file, indent=4, ensure_ascii=False)
        print(f"Saved file {save_target} successfully")


if __name__ == "__main__":
    main()
