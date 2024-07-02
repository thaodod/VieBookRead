## this is to filter out tiny mis-detected figures and make surya.csv
## input is surya-o (where containing all .json files from raw surya code)
## No Picture label exist in json files
import os
import json
import csv
import argparse


def process_json_file(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)

    results = []
    filename = os.path.splitext(os.path.basename(filepath))[0]

    for page_key, content in data.items():
        for page in content:
            image_bbox = page["image_bbox"]
            image_width = image_bbox[2] - image_bbox[0]
            image_height = image_bbox[3] - image_bbox[1]
            image_area = image_width * image_height

            valid_figures = False
            for bbox_data in page["bboxes"]:
                if bbox_data["label"] == "Figure":
                    x1, y1, x2, y2 = bbox_data["bbox"]
                    w = x2 - x1
                    h = y2 - y1
                    area = w * h

                    if (
                        w >= 0.03 * image_width
                        and h >= 0.0229 * image_height
                        and area >= 0.0032 * image_area
                    ):
                        valid_figures = True
                        break

            answer = "yes" if valid_figures else "no"
            results.append([f"{filename}/{page_key}.jpg", answer])

    return results


def main(input_dir, output_csv):
    all_results = []

    for json_file in os.listdir(input_dir):
        if json_file.endswith(".json"):
            filepath = os.path.join(input_dir, json_file)
            all_results.extend(process_json_file(filepath))

    with open(output_csv, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["filepath", "answer"])
        csvwriter.writerows(all_results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process JSON files to extract figure info and output a CSV file."
    )
    parser.add_argument(
        "--input-dir",
        type=str,
        required=True,
        help="Directory containing the JSON files",
    )
    parser.add_argument("--output", type=str, required=True, help="Output CSV file")

    args = parser.parse_args()
    main(args.input_dir, args.output)
