# POST spelling correction by Sonnet 3.5

import argparse
import os
import glob

import json
import multiprocessing as mp
from others.spell_correct_sonnet import correct


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

    for para in para_list:
        status = para["status"]
        if status in ["invalid", "corrected", "perfect"]:
            continue

        para_text = para["content"]
        if len(para_text.strip()) < 10 or len(para_text.strip()) > 550:
            # skip spell correct for too short or too long.
            continue # later, at final, just get 'original'

        s_score = para.get("search-sco", [None])[0] if para.get("search-sco") else None
        if s_score is not None and s_score >= 90:
            # skip as already "good"
            continue # later, at final, just get 'original'

        para_modified = correct(para_text)

        if para_modified == para_text:
            para["status_p"] = "intact"
            continue
        elif para_modified is False:
            para["status_p"] = "intact"
            continue
        else:
            para["status_p"] = "modified"
            para["content_s"] = para_modified

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
    with mp.Pool(processes=mp.cpu_count() - 12) as pool:
        pool.starmap(
            process_json,
            [(args, js_path) for js_path in json_paths],
        )


if __name__ == "__main__":
    main()
