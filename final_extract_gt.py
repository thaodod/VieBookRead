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
    out_list = []

    for para in para_list:
        status = para["status"]
        status_post = para.get("status_post", None)

        if status == "perfect" or status_post in ["skip", "intact"]:
            text = para["content"]
            out_list.append(text)
            continue

        if status == "corrected":
            text = para["content_"]
            out_list.append(text)
            continue

        if status_post == "modified":
            text = para["content_spell"]
            out_list.append(text)
            continue

    if not os.path.exists(args.o):
        os.makedirs(args.o, exist_ok=True)

    save_target = os.path.join(args.o, js_basename)
    with open(save_target, "w", encoding="utf-8") as file:
        json.dump(out_list, file, indent=2, ensure_ascii=False)
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
