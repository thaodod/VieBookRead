import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import argparse
import re
import json
import os

def get_text_from_epub(file_path):
    book = epub.read_epub(file_path, {"ignore_ncx": True})
    
    all_text = []

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = item.get_body_content().decode('utf-8')
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text()
            all_text.append(text)
    
    return "\n".join(all_text)

def trim_extra_newlines(text):
    # Replace multiple newlines with a maximum of two
    trimmed_text = re.sub(r'\n{3,}', '\n\n', text)
    return trimmed_text

def extract_content_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        paragraphs = data.get('paragraphs', [])
        content_list = [paragraph.get('content', '') for paragraph in paragraphs]
        return content_list

def process_directory(dir_path):
    all_content = []
    files = [f for f in os.listdir(dir_path) if f.endswith('.json')]
    
    # Sort files based on the numeric part of the filename
    files.sort(key=lambda x: int(re.search(r'page_(\d+).json', x).group(1)))
    
    for file in files:
        file_path = os.path.join(dir_path, file)
        content_list = extract_content_from_json(file_path)
        all_content.extend(content_list)
        
    return all_content

def main():
    parser = argparse.ArgumentParser(description='Extract and print text from an EPUB file.')
    parser.add_argument('epub', type=str, help='Path to the EPUB file')
    parser.add_argument('draft', type=str, help='Path to the draft folder')
    parser.add_argument('--debug', type=str, help='Path to write epub text to see')
    
    
    args = parser.parse_args()
    
    gt = get_text_from_epub(args.epub)
    trim_gt = trim_extra_newlines(gt)
    f = open(args.debug, "w")
    f.write(trim_gt)
    f.close()
    
    pages = process_directory(args.draft)
    print(pages[0])

if __name__ == '__main__':
    main()
