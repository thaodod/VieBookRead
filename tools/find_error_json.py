import os
import json

def validate_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
        return True
    except json.JSONDecodeError:
        return False

def validate_json_files_in_directory(directory):
    total_files = 0
    error_files = 0
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                total_files += 1
                file_path = os.path.join(root, file)
                if not validate_json_file(file_path):
                    error_files += 1

    return total_files, error_files

# Example usage
directory = 'data/json_clean'
total_files, error_files = validate_json_files_in_directory(directory)
print(f"Total JSON files: {total_files}")
print(f"Files with errors: {error_files}")
