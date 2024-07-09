import os
import json
import csv
import argparse

## input is the surya-o folder where contains all raw json files from surya run.


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
            valid_tables = False

            for bbox_data in page["bboxes"]:
                if bbox_data["label"] == "Figure":
                    x1, y1, x2, y2 = bbox_data["bbox"]
                    w = x2 - x1
                    h = y2 - y1
                    area = w * h

                    if (
                        w >= 0.01 * image_width
                        and h >= 0.023 * image_height
                        and area >= 0.0035 * image_area
                    ):
                        valid_figures = True

                elif bbox_data["label"] == "Table":
                    x1, y1, x2, y2 = bbox_data["bbox"]
                    w = x2 - x1
                    h = y2 - y1
                    area = w * h

                    if (
                        w >= 0.01 * image_width
                        and h >= 0.023 * image_height
                        and area >= 0.003 * image_area
                    ):
                        valid_tables = True

                if valid_figures and valid_tables:
                    break

            figure_answer = "yes" if valid_figures else "no"
            table_answer = "yes" if valid_tables else "no"
            results.append([f"{filename}/{page_key}.jpg", figure_answer, table_answer])

    return results


def main(input_dir, output_csv):
    all_results = []

    for root, dirs, files in os.walk(input_dir):
        for json_file in files:
            if json_file.endswith(".json"):
                filepath = os.path.join(root, json_file)
                all_results.extend(process_json_file(filepath))

    with open(output_csv, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["filepath", "figure_exists", "table_exists"])
        csvwriter.writerows(all_results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process JSON files to extract figure and table info and output a CSV file."
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Directory containing the JSON files",
    )
    parser.add_argument("--output", type=str, required=True, help="Output CSV file")

    args = parser.parse_args()
    main(args.input, args.output)