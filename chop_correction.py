import argparse
import os
import glob

import json
import multiprocessing as mp
from others.crop import find_best_match, count_w


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

    for para in para_list:
        status = para["status"]

        if status == "corrected":
            para_text = para["content"]
            para_llm = para["content_"]
            best_match, h_score = find_best_match(para_text, para_llm)
            para["content_c"] = best_match
            para["halu_score"] = h_score
            if count_w(best_match) < count_w(para_llm):
                print("cut off ", js_path)

            if count_w(para_text) > count_w(best_match) + 5:
                # when OCR is longer than chop off
                print("OCR longer ", js_path)

    if not os.path.exists(args.o):
        os.makedirs(args.o, exist_ok=True)

    save_target = os.path.join(args.o, js_basename)
    with open(save_target, "w", encoding="utf-8") as file:
        json.dump(para_list, file, indent=4, ensure_ascii=False)
    # print(f"Saved file {save_target} successfully")


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
