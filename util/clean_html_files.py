import os
import argparse
from bs4 import BeautifulSoup
import re
from unidecode import unidecode


def clean_text(text):
    # Replace spaces and zero-width characters with a single space
    space_chars = "\xa0\u2002\u2003\u200B\u200C\u200D\u2009\u200A\u2004\u2005\u2006\u2007\u2008\u202F"
    for char in space_chars:
        text = text.replace(char, " ")

    # Replace quotation marks with ASCII equivalents
    text = text.replace("\u201C", '"').replace("\u201D", '"')
    text = text.replace("\u2018", "'").replace("\u2019", "'")

    # Replace dashes with ASCII hyphen
    text = text.replace("\u2013", "-").replace("\u2014", "-")

    # Replace ellipsis with three dots
    text = text.replace("\u2026", "...")

    # Remove byte order mark
    text = text.replace("\ufeff", "")

    # Replace non-breaking hyphen with regular hyphen
    text = text.replace("\u2011", "-")

    # Collapse multiple spaces into one
    text = re.sub(r"\s+", " ", text)

    return text


def clean_html_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Remove the XML declaration
    content = re.sub(r"<\?xml[^>]+\?>\s*", "", content, flags=re.DOTALL)

    # Parse the HTML
    soup = BeautifulSoup(content, "html.parser")

    # Get all text nodes
    texts = soup.find_all(text=True)

    # Clean all text nodes
    for text in texts:
        if text.parent.name not in [
            "script",
            "style",
        ]:  # avoid script and style contents
            new_text = clean_text(text)
            text.replace_with(new_text)

    # Save the cleaned content
    cleaned_content = str(soup)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(cleaned_content)

    print(f"Cleaned: {input_path} -> {output_path}")


def process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith((".html", ".xhtml", ".htm")):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_dir)
                relative_path = unidecode(relative_path)
                output_path = os.path.join(output_dir, relative_path)
                clean_html_file(input_path, output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Clean HTML files of special characters."
    )
    parser.add_argument("input_dir", help="Input directory containing HTML files")
    parser.add_argument("output_dir", help="Output directory for cleaned HTML files")
    args = parser.parse_args()

    input_dir = os.path.abspath(args.input_dir)
    output_dir = os.path.abspath(args.output_dir)

    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        return

    if input_dir == output_dir:
        print("Error: Input and output directories must be different.")
        return

    print(f"Processing files from {input_dir}")
    print(f"Saving cleaned files to {output_dir}")

    process_directory(input_dir, output_dir)

    print("Processing complete.")


if __name__ == "__main__":
    main()
