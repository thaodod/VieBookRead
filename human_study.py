import argparse
import os
import random
import shutil
import math
from pathlib import Path


def is_even(src_path):
    base_n = Path(src_path).stem
    last_c = base_n[-1]
    if int(last_c) % 2 == 0:
        return True
    else:
        return False


def stratified_sampling(input_dir, in_final, in_vng, out, total, sample_size):
    # Get all subdirectories
    subdirs = [
        f for f in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, f))
    ]
    subdirs.sort()

    # Calculate sample size for each subdirectory
    samples_per_subdir = {
        subdir: math.ceil(
            sample_size * len(os.listdir(os.path.join(input_dir, subdir))) / total
        )
        for subdir in subdirs
    }

    # Adjust sample sizes to ensure total is exactly sample_size
    while sum(samples_per_subdir.values()) > sample_size:
        max_subdir = max(samples_per_subdir, key=samples_per_subdir.get)
        samples_per_subdir[max_subdir] -= 1

    # Perform sampling and copy files
    sampled_files = []
    for subdir in subdirs:
        subdir_path = os.path.join(input_dir, subdir)
        files = [f for f in os.listdir(subdir_path) if f.lower().endswith(".jpg")]
        sample = random.sample(files, samples_per_subdir[subdir])
        for file in sample:
            new_name = f"{subdir}_{file}"
            sampled_files.append((os.path.join(subdir_path, file), new_name))

    # Create output directory structure and copy files
    chunk_size = 30
    for i, (src_path, new_name) in enumerate(sampled_files):
        chunk_num = i // chunk_size
        chunk_dir = os.path.join(out, f"chunk{chunk_num:02d}")
        os.makedirs(chunk_dir, exist_ok=True)

        src_final = src_path.replace(input_dir, in_final).replace(".jpg", ".json")
        src_vng = src_path.replace(input_dir, in_vng).replace(".jpg", ".json")

        dst_path = os.path.join(chunk_dir, new_name)
        # for image file
        if is_even(src_path):
            final_t = "_L"
            vng_t = "_R"
        else:
            final_t = "_R"
            vng_t = "_L"

        dst_final = os.path.splitext(dst_path)[0] + final_t + ".json"
        dst_vng = os.path.splitext(dst_path)[0] + vng_t + ".json"
        shutil.copy2(src_path, dst_path)
        shutil.copy2(src_final, dst_final)
        shutil.copy2(src_vng, dst_vng)

    print(f"Sampled, copied {len(sampled_files)} files to {out}")


def main():
    parser = argparse.ArgumentParser(description="correct spelling by VNG")
    parser.add_argument("inp_img", help="dir to load img")
    parser.add_argument("inp_final", help="dir to load img")
    parser.add_argument("inp_vng", help="dir to load img")
    parser.add_argument("out", help="root for output")

    total_files = 25585
    sample_size = 1025

    args = parser.parse_args()

    stratified_sampling(
        args.inp_img, args.inp_final, args.inp_vng, args.out, total_files, sample_size
    )


if __name__ == "__main__":
    main()
