import argparse
from bs4 import BeautifulSoup
import tiktoken
from lxml.html.clean import Cleaner
from lxml.html import tostring, fromstring


def contain_alpha_num(s):
    return any(c.isalpha() or c.isdigit() for c in s)


def clean_class(html_content):
    html = fromstring(html_content)
    for element in html.xpath("//*[@class or @lang or @href or @title]"):
        element.attrib.pop("class", None)
        element.attrib.pop("lang", None)
        element.attrib.pop("title", None)
        if "href" in element.attrib:
            element.attrib["href"] = "#"

    return tostring(html, encoding="unicode", method="html")


def clean_htm(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        if content.lstrip().startswith("<?xml version="):
            content = "\n".join(content.split("\n")[1:])

        cleaner = Cleaner(
            page_structure=False,
            meta=True,
            embedded=True,
            style=True,
            processing_instructions=True,
            inline_style=True,
            scripts=True,
            javascript=True,
            comments=True,
            frames=True,
            forms=True,
            annoying_tags=True,
            remove_unknown_tags=True,
        )
        return clean_class(cleaner.clean_html(content))


def clean_nested(content):
    soup = BeautifulSoup(content, "html.parser")
    # Remove redundant nested spans or similar elements
    for tag in soup.find_all():
        # Continue only if the tag has at least one child
        while (
            tag.contents and len(tag.contents) == 1 and tag.contents[0].name == tag.name
        ):
            # Ensure the tag does not have significant attributes
            if not any(tag.attrs.get(attr) for attr in ["href", "src"]):
                tag.unwrap()
            else:
                break

    return str(soup)


def clean_html_txt(text):
    cleaner = Cleaner(
        page_structure=False,
        embedded=True,
        style=True,
        processing_instructions=True,
        inline_style=True,
        scripts=True,
        javascript=True,
        comments=True,
        frames=True,
        forms=True,
        annoying_tags=True,
        remove_unknown_tags=True,
    )
    return clean_class(cleaner.clean_html(text))


def count_token(content):
    # Initialize the tokenizer
    tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
    return len(tokenizer.encode(content))


def compose_html(paragraphs):
    para_txt = [str(paragraph) for paragraph in paragraphs]
    para_txt = ' '.join(para_txt)
    html_template = f"""<html><head><meta charset="UTF-8"></head><body>{para_txt}</body></html>"""
    return html_template


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="pick html file")
    args = parser.parse_args()
    html_content = clean_htm(args.source)
    print(html_content)
    print("number of token: ", count_token(html_content))


if __name__ == "__main__":
    main()
