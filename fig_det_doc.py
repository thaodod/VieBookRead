import sys
import os
import glob
import argparse
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "DocOwl1.5")))

from docowl_infer import DocOwlInfer

model_path = "mPLUG/DocOwl1.5-Omni"
docowl = DocOwlInfer(ckpt_path=model_path, anchors="grid_9", add_global_img=True)
print("load model from ", model_path)

QUERY = "is there a picture or drawing in this scanned document ?"
## is there a visual figure in this scanned document ?


def check_yes_no(input_string: str) -> str:
    if input_string.lower().startswith("yes"):
        return "yes"
    elif input_string.lower().startswith("no"):
        return "no"
    else:
        return "yes"  # not sure


def process_images(source, query, output_file):
    results = []

    # Traverse the directory and its subdirectories
    for root, _, files in os.walk(source):
        for file in files:
            if file.lower().endswith(".jpg"):
                image_file = os.path.join(root, file)
                relative_image_path = os.path.relpath(image_file, source)
                # Apply the inference function
                answer = check_yes_no(docowl.inference(image_file, query))
                # Append the result as a tuple (relative_image_path, answer)
                results.append((relative_image_path, answer))

    sorted_results = sorted(results, key=lambda x: x[0])

    # Save results to a CSV file
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["filepath", "answer"])  # Write the header
        writer.writerows(sorted_results)  # Write the data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process images and generate a CSV file."
    )
    parser.add_argument(
        "--source",
        type=str,
        required=True,
        help="Source directory containing the images",
    )
    parser.add_argument(
        "--o", type=str, required=True, help="Output path for the CSV file"
    )
    parser.add_argument("--query", type=str, default=QUERY, help="Query")

    args = parser.parse_args()

    process_images(args.source, args.query, args.o)
