import zipfile
import os
import argparse

def extract_html_from_epub(epub_path, output_folder):
    with zipfile.ZipFile(epub_path, 'r') as epub:
        for file in epub.namelist():
            if file.endswith('.html') or file.endswith('.xhtml'):
                epub.extract(file, output_folder)

def main():
    parser = argparse.ArgumentParser(description='Extract HTML files from an EPUB file.')
    parser.add_argument('epub_file', help='Path to the EPUB file')
    parser.add_argument('-o', '--output', default='extracted_html', 
                        help='Output directory for extracted HTML files (default: extracted_html)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    
    extract_html_from_epub(args.epub_file, args.output)
    print(f"HTML files extracted to {args.output}")

if __name__ == "__main__":
    main()