# This script to extract final annotation for releasing to public.
# After LLM-ref correct, chop off, reject_llm and spell correct by Sonnet
# NOTE, here, last time we clean last noises(where we forgot to clean last step):
# clean single-letter content located at 0, 1 (top bboxes) and -2 -1 (bottom bboxes)
# THEN (actually same time), we use below logic to extract final:
################################################################
# skip 'invalid' and above noises (i.e. don't take them)
# at "perfect" -> take original 'content'
# at "corrected" (still after reject_lm) -> take 'content_c'
# at other statuses ([skip, not_found, not_relevant, reject_lm_x]) -> take:
#       check 'status_p', if it is 'intact'   -> take original 'content'
#       check 'status_p', if it is 'modified' -> take 'content_s'
################################################################
# Also add size (dimension) of original image.

import argparse
import os
import glob

import json
import multiprocessing as mp
from pathlib import Path
from PIL import Image


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
    im_path = os.path.join(args.im_dir, Path(js_basename).stem + ".jpg")
    with Image.open(im_path) as img:
        width, height = img.size

    para_list = load_json(js_path)
    len_list = len(para_list)
    out_list = [{"w": width, "h": height}]  # add dict elements after the dim

    for idx, para in enumerate(para_list):
        status = para["status"]
        status_p = para.get("status_p", None)

        o_text = para["content"].strip()

        # skip final described noises
        if len(o_text) == 1 and status in {"skip", "not_found", "not_relevant"}:
            if o_text[0].isalpha() and (idx < 2 or idx > len_list - 3):
                continue

        if status == "invalid":
            continue

        if status == "perfect" or status == "intact":
            text = o_text

        elif status == "corrected":
            text = para["content_c"].strip()

        elif status.startswith("reject") or status in {
            "skip",
            "not_found",
            "not_relevant",
        }:
            if status_p == "intact" or status_p is None:
                text = o_text
            elif status_p == "modified":
                text = para["content_s"].strip()
            else:
                print("ERR1")
        else:
            print("ERR2")  # if there new status, check again!!

        poly = para["polygon"]
        out_list.append({"text": text, "polygon": poly})

    if not os.path.exists(args.o):
        os.makedirs(args.o, exist_ok=True)

    save_target = os.path.join(args.o, js_basename)
    with open(save_target, "w", encoding="utf-8") as file:
        json.dump(out_list, file, indent=2, ensure_ascii=False)
    print(f"Saved file {save_target} successfully")


# Work for each book, not for all at the same time.
def main():
    parser = argparse.ArgumentParser(description="final extraction")
    parser.add_argument("im_dir", help="dir to original images to get size")
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
