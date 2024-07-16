import argparse
import os
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from util.lang_detect import is_meaning_text
import json


def search_html_files(directory, query, threshold=70, block_size=4, padding=1):
    # List all HTML files in the directory
    html_files = [
        f for f in os.listdir(directory) if f.endswith((".html", ".xhtml", ".htm"))
    ]

    match_files = []

    for html_file in html_files:
        # Read the content of the HTML file
        with open(os.path.join(directory, html_file), "r", encoding="utf-8") as file:
            content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(content, "html.parser")
        paragraphs = soup.find_all(
            [
                "p",
                "div",
                "span",
                "li",
                "h1",
                "h2",
                "h3",
                "h4",
                "h5",
                "h6",
                "a",
                "td",
                "th",
                "caption",
                "pre",
            ]
        )  # Common tags containing text

        # Store the matching blocks with their scores and HTML
        matched_blocks = []

        # Calculate similarity scores for blocks of paragraphs
        for i in range(0, len(paragraphs), block_size):
            block = paragraphs[i : i + block_size]
            block_text = " ".join(paragraph.get_text() for paragraph in block)
            score = fuzz.partial_ratio(query, block_text)
            if score >= threshold:
                # Get the padded block
                start = max(0, i - padding)
                end = min(len(paragraphs), i + block_size + padding)
                padded_block = paragraphs[start:end]
                block_html = "".join(str(paragraph) for paragraph in padded_block)
                matched_blocks.append((block_html, score))

        if matched_blocks:
            # Calculate the average score for the document
            avg_score = sum(score for _, score in matched_blocks) / len(matched_blocks)
            match_files.append((html_file, avg_score, matched_blocks))

    # Sort the matching files by their average score in descending order
    match_files.sort(key=lambda x: x[1], reverse=True)

    return match_files


def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        # Skip the first element and extract 'content' values
        return data[1:]

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: '{file_path}' is not a valid JSON")
        return []


def main():
    parser = argparse.ArgumentParser(description="Search a folder ")
    parser.add_argument("source", help="html book directory")
    parser.add_argument("json", help="pick on processed azure json for that book")
    args = parser.parse_args()

    para_list = load_json(args.json)
    for para in para_list:
        para_text = para["content"]
        if not is_meaning_text(para_text):
            print("skip this query: ", para_text)
            continue
        print("query: ", para_text)
        match_files = search_html_files(args.source, para_text)

        if match_files:
            print("Ranked files:")
            for file, score, blocks in match_files:
                print(f"\nFile: {file}\nAverage Score: {score}")
                for block_html, b_score in blocks:
                    print(f"Score: {b_score}\nHTML: \n{block_html}\n")
        else:
            print("No matching found.")

        print("=============================")


if __name__ == "__main__":
    main()
