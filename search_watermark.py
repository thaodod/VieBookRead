import os
import json
import argparse

def search_text_in_json_files(root_dir, search_text):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(subdir, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)
                        if search_text_in_data(data, search_text):
                            print(f"Found '{search_text}' in file: {file_path}")
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {file_path}")
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

def search_text_in_data(data, search_text):
    if isinstance(data, dict):
        for key, value in data.items():
            if search_text_in_data(value, search_text):
                return True
    elif isinstance(data, list):
        for item in data:
            if search_text_in_data(item, search_text):
                return True
    elif isinstance(data, str):
        if search_text in data:
            return True
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search for text in JSON files within a directory.')
    parser.add_argument('--root', required=True, help='The root directory to search')
    parser.add_argument('--text', required=True, help='The text to search for')
    args = parser.parse_args()

    search_text_in_json_files(args.root, args.text)
