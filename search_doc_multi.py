import argparse
import os
import glob
from util.lang_detect import is_meaning_str
from util.count_token import (
    compose_html,
    contain_alpha_num,
    count_words,
)
from text_match import correct_text  # call LLM here.
import json
import multiprocessing as mp
from search_doc import search_html, load_dir, load_json


def process_json_file(args, in_js_path, file_content_pairs):
    js_basename = os.path.basename(in_js_path)
    meta, para_list = load_json(in_js_path)

    for para in para_list:
        para_text = para["content"]
        if not is_meaning_str(para_text) or count_words(para_text) <= 2:
            if not contain_alpha_num(para_text) and len(para_text) < 5:
                para["status"] = "invalid"
            else:
                para["status"] = "skip"
            continue

        match_files = search_html(file_content_pairs, para_text)

        if match_files:
            # highest sim score file is used to search
            _, _, blocks0 = match_files[0]
            block_cont, score = blocks0
            simple_html = compose_html(block_cont)
            if score == 100:
                correct_para = para_text
            else:
                correct_para = correct_text(simple_html, para_text, args.m)

            if correct_para:
                para["content_"] = correct_para
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


def main():
    parser = argparse.ArgumentParser(description="Search a folder ")
    parser.add_argument("source", help="dir to load all ref html files")
    parser.add_argument("json_dir", help="dir to load input json files")
    parser.add_argument("-o", help="where to save json files of a book")
    parser.add_argument("-m", default="gpt4", help="model to correct text")

    args = parser.parse_args()

    json_paths = glob.glob(os.path.join(args.json_dir, "*.json"))
    file_content_pairs = load_dir(args.source)

    # Use multiprocessing to process JSON files in parallel
    with mp.Pool(processes=mp.cpu_count() - 4) as pool:
        pool.starmap(
            process_json_file,
            [(args, in_js_path, file_content_pairs) for in_js_path in json_paths],
        )


if __name__ == "__main__":
    main()
