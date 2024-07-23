import argparse
import os
import glob
from bs4 import BeautifulSoup
from thefuzz import fuzz
from thefuzz import process
from util.lang_detect import is_meaning_str
from util.count_token import clean_html_txt, compose_html, contain_alpha_num
from util.extract_html import flatten_html
from text_match import text_correct  # call LLM here.
import json


def load_dir(dir):
    html_files = [f for f in os.listdir(dir) if f.endswith((".html", ".xhtml", ".htm"))]
    file_n_contents = []
    for html_file in html_files:
        with open(os.path.join(dir, html_file), "r", encoding="utf-8") as file:
            content = clean_html_txt(file.read())
            htm_para_s = flatten_html(content)
        file_n_contents.append((html_file, htm_para_s))

    return file_n_contents


def render_blk(paragraph):
    mini_soup = BeautifulSoup(paragraph, "html.parser")
    return mini_soup.get_text()


def search_html_files(f_content_pairs, query, threshold=65, block_size=1):
    matched_files = []

    for file, paragraphs in f_content_pairs:
        curr_blk_size = block_size

        # Store the highest scored block with its score and HTML
        highest_scored_block = None
        highest_score = 0

        num_paragraphs = len(paragraphs)
        if num_paragraphs < curr_blk_size:
            curr_blk_size = num_paragraphs
        for i in range(num_paragraphs - curr_blk_size + 1):
            block = paragraphs[i : i + curr_blk_size]
            block_text = " ".join(render_blk(paragraph) for paragraph in block)
            score = fuzz.partial_ratio(query.lower(), block_text.lower())
            score_o = fuzz.partial_ratio(query, block_text)
            if score < score_o:
                score = score_o
            if score >= threshold and score > highest_score:
                highest_scored_block = (block, score)
                highest_score = score
            if highest_score > 95:  # no need to search more block
                break

        if highest_scored_block:
            matched_files.append((file, highest_score, highest_scored_block))

        if highest_score > 95:  # no need to search more file
            break

    # Sort matched files by their score in descending order
    matched_files.sort(key=lambda x: x[1], reverse=True)

    return matched_files


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
    file_content_pairs = load_dir(args.source)

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

            match_files = search_html_files(file_content_pairs, para_text)

            if match_files:
                # highest sim score file is used to search
                _, _, blocks0 = match_files[0]
                block_cont, _ = blocks0
                simple_html = compose_html(block_cont)
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
