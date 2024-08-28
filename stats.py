import os
import json

root_directory = 'data/reject_lm/'
search_string = '"status": "corrected"'

def search_string_in_json_files(root_dir, search_string):
    total_count = 0
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        occurrences = json.dumps(data).count(search_string)
                        if occurrences > 0:
                            total_count += occurrences
                    except json.JSONDecodeError:
                        print(f'Error decoding JSON in file {file_path}')
    print(f'Total occurrences of "{search_string}": {total_count}')


search_string_in_json_files(root_directory, search_string)
