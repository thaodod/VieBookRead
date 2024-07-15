import os
from bs4 import BeautifulSoup, NavigableString, Tag
import re
import argparse
import copy


def safe_copy(elem):
    if elem is None:
        return None
    try:
        if isinstance(elem, NavigableString):
            return type(elem)(elem)
        if isinstance(elem, Tag):
            return copy.copy(elem)
        return elem
    except:
        print(f"Warning: Could not copy element {elem}")
        return None


def extract_h2_sections(input_file, output_dir):
    # Read the input HTML file
    with open(input_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")

    # Find all h2 elements
    h2_elements = soup.find_all("h2")

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Extract content for each h2 element
    for index, h2 in enumerate(h2_elements, start=1):
        extracted_soup = BeautifulSoup("<html><body></body></html>", "html.parser")
        body = extracted_soup.body

        # Find the parent h1
        parent_h1 = h2.find_previous("h1")

        # Add content before the first h1 if this is the first h2
        if index == 1:
            first_h1 = soup.find("h1")
            if first_h1:
                for elem in first_h1.previous_siblings:
                    copied = safe_copy(elem)
                    if copied:
                        body.append(copied)

        # Add the parent h1
        if parent_h1:
            copied_h1 = safe_copy(parent_h1)
            if copied_h1:
                body.append(copied_h1)

        # Add content between h1 and h2 if this is the first h2 after an h1
        prev_h2 = h2.find_previous("h2")
        if not prev_h2 or prev_h2.find_previous("h1") != parent_h1:
            for elem in h2.previous_siblings:
                if elem == parent_h1:
                    break
                copied = safe_copy(elem)
                if copied:
                    body.append(copied)

        # Add the h2 and its content
        copied_h2 = safe_copy(h2)
        if copied_h2:
            body.append(copied_h2)

        for elem in h2.next_siblings:
            if isinstance(elem, Tag) and elem.name in ["h1", "h2"]:
                break
            copied = safe_copy(elem)
            if copied:
                body.append(copied)

        # Generate a file name based on the h2 content
        file_name = re.sub(r"[^\w\s-]", "", h2.get_text().strip()).lower()
        file_name = re.sub(r"[-\s]+", "-", file_name)
        output_file = os.path.join(output_dir, f"{index:02d}_{file_name[:50]}.html")

        # Write the extracted content to a file
        with open(output_file, "w", encoding="utf-8") as f:
            content = str(extracted_soup)
            f.write(content)
            print(f"Writing file: {output_file}")
            if len(content) < 100:  # Print short content for debugging
                print(f"Content: {content}")

    print(f"Extraction complete. Files saved in {output_dir}")


def extract_h1_without_h2(input_file, output_dir):
    # Read the input HTML file
    with open(input_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")

    # Find all h1 elements
    h1_elements = soup.find_all("h1")

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Extract content for each h1 element without a following h2
    for index, h1 in enumerate(h1_elements, start=1):
        has_h2 = False
        content_elements = []

        for elem in h1.next_siblings:
            if isinstance(elem, Tag):
                if elem.name == "h1":
                    break
                if elem.name == "h2":
                    has_h2 = True
                    break
            content_elements.append(elem)

        if not has_h2:
            extracted_soup = BeautifulSoup("<html><body></body></html>", "html.parser")
            body = extracted_soup.body

            copied_h1 = safe_copy(h1)
            if copied_h1:
                body.append(copied_h1)

            for elem in content_elements:
                copied = safe_copy(elem)
                if copied:
                    body.append(copied)

            # Generate a file name based on the h1 content
            file_name = re.sub(r"[^\w\s-]", "", h1.get_text().strip()).lower()
            file_name = re.sub(r"[-\s]+", "-", file_name)
            output_file = os.path.join(
                output_dir, f"h1_{index:02d}_{file_name[:50]}.html"
            )

            # Write the extracted content to a file
            with open(output_file, "w", encoding="utf-8") as f:
                content = str(extracted_soup)
                f.write(content)
                print(f"Writing file: {output_file}")
                if len(content) < 100:  # Print short content for debugging
                    print(f"Content: {content}")

    print(f"Extraction complete. Files saved in {output_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract HTML sections based on h2 headings"
    )
    parser.add_argument("source", help="Path to the input HTML file")
    parser.add_argument("out", help="Path to the output directory")
    args = parser.parse_args()

    extract_h2_sections(args.source, args.out)
    extract_h1_without_h2(args.source, args.out)


if __name__ == "__main__":
    main()
