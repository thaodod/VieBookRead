import os
import json
import codecs

def check_empty_json(root_folder):
    empty_files = []
    
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with codecs.open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if not data:
                            empty_files.append(file_path)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {file_path}")
                except UnicodeDecodeError:
                    print(f"Unicode decode error in file: {file_path}. The file might not be in UTF-8 encoding.")
                except Exception as e:
                    print(f"Error reading file {file_path}: {str(e)}")
    
    return empty_files

# Replace 'D:/DATA/output' with the actual path to your root folder
root_folder = 'D:/DATA/output_json'
empty_json_files = check_empty_json(root_folder)

if empty_json_files:
    print("The following JSON files are empty:")
    for file in empty_json_files:
        print(file)
else:
    print("No empty JSON files found.")