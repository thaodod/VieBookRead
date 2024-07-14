import zipfile
import os
import argparse
import re


def extract_html_from_epub(epub_path, output_folder):
    with zipfile.ZipFile(epub_path, "r") as epub:
        for file in epub.namelist():
            if file.endswith((".html", ".xhtml", ".htm")):
                # Extract the file content
                content = epub.read(file)

                filename = os.path.basename(file)

                # Ensure unique filenames
                counter = 1
                new_filename = filename
                while os.path.exists(os.path.join(output_folder, new_filename)):
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_{counter}{ext}"
                    counter += 1

                with open(os.path.join(output_folder, new_filename), "wb") as f:
                    f.write(content)


def process_epub_directory(source_dir, output_base_dir):
    for filename in os.listdir(source_dir):
        if filename.endswith(".epub"):
            match = re.match(r"(\d{3})__", filename)
            if match:
                epub_id = match.group(1)
                epub_path = os.path.join(source_dir, filename)
                output_folder = os.path.join(output_base_dir, epub_id)

                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)

                extract_html_from_epub(epub_path, output_folder)
                print(f"Processed {filename} -> {output_folder}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract HTML files from EPUB files in a directory."
    )
    parser.add_argument("source", help="Directory containing EPUB files")
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Base output directory for extracted HTML files",
    )

    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    process_epub_directory(args.source, args.output)
    print(f"All EPUB files processed. Output in {args.output}")


if __name__ == "__main__":
    main()
