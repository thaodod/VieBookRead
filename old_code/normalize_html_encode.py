import os
import unicodedata

def normalize_html_file(file_path):
    try:
        # Read HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Normalize content
        normalized_content = unicodedata.normalize('NFC', content)
        
        # Write back the normalized content to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(normalized_content)
        
        print(f'Normalized: {file_path}')
    except Exception as e:
        print(f'Failed to normalize {file_path}: {e}')

def normalize_html_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".html", ".xhtml", ".htm")):
                file_path = os.path.join(root, file)
                normalize_html_file(file_path)

if __name__ == '__main__':
    root_directory = 'D:\\DATA\\html_f'
    normalize_html_files_in_directory(root_directory)
