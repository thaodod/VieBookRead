import json
import re


def reorder_jsonl(file_path, output_file):
    # Read the JSONL file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Parse each line into a JSON object
    data = [json.loads(line) for line in lines]

    # Function to extract directory and page number from the filepath
    def get_sort_key(json_obj):
        filepath = json_obj["filepath"]
        match = re.match(r"(\d+)/page_(\d+)\.jpg", filepath)
        if match:
            dir_number = int(match.group(1))
            page_number = int(match.group(2))
            return (dir_number, page_number)
        return (0, 0)  # Default in case of unexpected format

    # Sort data by the extracted directory and page number
    data_sorted = sorted(data, key=get_sort_key)

    # Write the sorted data back to a new JSONL file
    with open(output_file, "w") as file:
        for entry in data_sorted:
            file.write(json.dumps(entry) + "\n")


# Example usage
reorder_jsonl("yolo-final.jsonl", "sorted_file.jsonl")
