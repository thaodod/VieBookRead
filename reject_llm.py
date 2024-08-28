import argparse
import os
import glob

import json
import multiprocessing as mp
from others.crop import max_ed
from underthesea import sent_tokenize, word_tokenize

# this to reject LLM corrected para if they have too much signed of halu.
# we also clean up "skip" status for case like 1, ! and so on. by update invalid.
# after that, we can do spelling correct lastly.


def first_last(paragraph):
    sents = sent_tokenize(paragraph)
    first_sent = sents[0] if sents else None
    last_sent = sents[-1] if len(sents) > 1 else first_sent

    return first_sent, last_sent


def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError:
        print(f"Error: '{file_path}' is not a valid JSON")
        return None


def check_gap(origin, chop):
    origin_l = len(word_tokenize(origin))
    chop_l = len(word_tokenize(chop))
    gap = abs(origin_l - chop_l)
    if origin_l <= 10 and gap <= 4:
        return True
    if 10 < origin_l <= 15 and gap <= 5:
        return True
    if 15 < origin_l <= 25 and gap <= 6:
        return True
    if 25 < origin_l <= 35 and gap <= 7:
        return True
    if 35 < origin_l <= 50 and gap <= 8:
        return True
    if 50 < origin_l <= 60 and gap <= 9:
        return True
    if 60 < origin_l <= 100 and gap <= 10:
        return True
    if 100 < origin_l <= 200 and gap < 14:
        return True
    if 200 > origin_l and gap < 18:
        return True
    return False


def check_first_last(origin, chop):
    f_o, l_o = first_last(origin)
    f_c, l_c = first_last(chop)

    if len(word_tokenize(f_o)) <= 4 or len(word_tokenize(l_o)) <= 4:
        # too short to evaluate as original might have many "."
        return True

    first_ed = max_ed(f_o, f_c)
    last_ed = max_ed(l_o, l_c)

    return first_ed > 0.68 and last_ed > 0.68


def process_json(args, js_path):
    js_basename = os.path.basename(js_path)
    para_list = load_json(js_path)
    len_para = len(para_list)

    for index, para in enumerate(para_list):
        status = para["status"]
        if status == "corrected":
            para_text = para["content"]
            para_chop = para["content_c"]
            h_score = para["halu_score"]
            s_score = para["search-sco"][0]

            if h_score < 0.84 and s_score > 90:
                para["status"] = "reject_lm_1"

            if h_score < 0.9 and s_score >= 93:
                para["status"] = "reject_lm_2"

            if h_score < 0.84 and s_score < 84:
                if not check_gap(para_text, para_chop):
                    para["status"] = "reject_lm_3"

                if not check_first_last(para_text, para_chop):
                    para["status"] = "reject_lm_4"

        if status == "skip" or status == "not_found" or "not_relevant":
            # check valid: noise like '1' or fake '11' or '1.' '.1'
            para_text = para["content"].strip()
            if para_text == "1" or para_text == "1." or para_text == ".1":
                para["status"] = "invalid"

            if para_text == "11" and (1 < index < len_para - 1):
                para["status"] = "invalid"

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
