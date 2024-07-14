import argparse
from bs4 import BeautifulSoup
import os


def split_html_file(input_file, output_dir):
    # Read the input HTML file
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(content, "html.parser")

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Initialize variables
    current_chapter = []
    current_subchapter = []
    chapter_number = 0
    subchapter_number = 0

    # Iterate through all elements in the body
    for element in soup.body.children:
        if element.name == "h1":
            # Save previous chapter and subchapter if they exist
            if current_subchapter:
                save_subchapter(
                    current_subchapter, chapter_number, subchapter_number, output_dir
                )
                current_subchapter = []
            if current_chapter:
                save_chapter(current_chapter, chapter_number, output_dir)
            chapter_number += 1
            subchapter_number = 0
            current_chapter = [str(element)]
            current_subchapter = [str(element)]
        elif element.name == "h2":
            # Save previous subchapter if it exists
            if current_subchapter:
                save_subchapter(
                    current_subchapter, chapter_number, subchapter_number, output_dir
                )
            subchapter_number += 1
            current_subchapter = [str(element)]
            current_chapter.append(str(element))
        else:
            if chapter_number == 0:
                chapter_number = 1
            if subchapter_number == 0:
                subchapter_number = 1
            current_chapter.append(str(element))
            current_subchapter.append(str(element))

    # Save the last subchapter and chapter
    if current_subchapter:
        save_subchapter(
            current_subchapter, chapter_number, subchapter_number, output_dir
        )
    if current_chapter:
        save_chapter(current_chapter, chapter_number, output_dir)


def save_chapter(chapter_content, chapter_number, output_dir):
    save_html_file(chapter_content, f"chapter_{chapter_number}", output_dir)


def save_subchapter(subchapter_content, chapter_number, subchapter_number, output_dir):
    save_html_file(
        subchapter_content, f"chapter_{chapter_number}_{subchapter_number}", output_dir
    )


def save_html_file(content, filename, output_dir):
    # Create a new HTML document
    soup = BeautifulSoup(
        "<!DOCTYPE html><html><head></head><body></body></html>", "html.parser"
    )

    # Add the content to the body
    for element in content:
        soup.body.append(BeautifulSoup(element, "html.parser"))

    # Save the file
    output_file = os.path.join(output_dir, f"{filename}.html")
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(str(soup))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="pick html file")
    parser.add_argument("out", help="pick output dir")
    args = parser.parse_args()
    split_html_file(args.source, args.out)


if __name__ == "__main__":
    main()
