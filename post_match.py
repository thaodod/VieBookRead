# POST matching and text correction by LM
# remove invalid
# remove skip string with single 1 alphaletter (but keep number)
# checking spelling for skip/not_relevant/not_found/intact
# if text is spelling correct already, we left them intact,
# else, we correct spelling by LLM with hint that the language is could be in Vietnamese, English, French, Chinese
# and also given an nearby paragraph (on the same page) which is correct/perfect if available.


import argparse
import os
import glob

import json
import multiprocessing as mp
from util.lm_util import is_spelling_correct, fix_spelling
from util.count_token import has_chinese
from thefuzz import fuzz


def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError:
        print(f"Error: '{file_path}' is not a valid JSON")
        return None


def process_json(args, js_path):
    js_basename = os.path.basename(js_path)

    para_list = load_json(js_path)
    nearby = []

    for para in para_list:
        status = para["status"]
        if status == "perfect":
            nearby.append(para["content"])

        if status == "corrected":
            nearby.append(para["content_"])

    for para in para_list:
        status = para["status"]
        if status in ["invalid", "corrected", "perfect"]:
            continue

        para_text = para["content"]
        if status == "skip" and len(para_text.strip()) < 10:
            para["status_post"] = "skip"
            continue

        if has_chinese(para_text):
            para["status_post"] = "skip"
            # with chinese, often hallucination, so skip
            continue

        if is_spelling_correct(para_text):
            para["status_post"] = "intact"
            continue

        nearby = [
            seq
            for seq in nearby
            if fuzz.partial_ratio(seq.lower(), para_text.lower()) > 70
        ]
        para_modified = fix_spelling(para_text, " ".join(nearby))
        if para_modified == para_text:
            para["status_post"] = "intact"
            continue
        
        para["status_post"] = "modified"
        para["content_spell"] = para_modified

    if not os.path.exists(args.o):
        os.makedirs(args.o, exist_ok=True)

    save_target = os.path.join(args.o, js_basename)
    with open(save_target, "w", encoding="utf-8") as file:
        json.dump(para_list, file, indent=4, ensure_ascii=False)
    print(f"Saved file {save_target} successfully")


# Work for each book, not for all at the same time.
def main():
    parser = argparse.ArgumentParser(description="postprocessing after matching")
    parser.add_argument("json_dir", help="dir to load input json files")
    parser.add_argument("o", help="where to out/save json files")

    args = parser.parse_args()

    json_paths = glob.glob(os.path.join(args.json_dir, "*.json"))

    # Use multiprocessing to process JSON files in parallel
    with mp.Pool(processes=mp.cpu_count() - 4) as pool:
        pool.starmap(
            process_json,
            [(args, js_path) for js_path in json_paths],
        )


if __name__ == "__main__":
    main()
