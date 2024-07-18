import argparse
from bs4 import BeautifulSoup
import tiktoken
from lxml.html.clean import Cleaner
from lxml.html import tostring, fromstring


def contain_alpha_num(s):
    return any(c.isalpha() or c.isdigit() for c in s)


def clean_class(html_content):
    html = fromstring(html_content)
    for element in html.xpath("//*[@class or @lang]"):
        element.attrib.pop("class", None)
        element.attrib.pop("lang", None)

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


def complete_html(partial_html):
    soup = BeautifulSoup(
        '<!DOCTYPE html><html><head><meta charset="UTF-8"></head><body></body></html>',
        "html.parser",
    )

    # Parse the partial HTML
    partial_soup = BeautifulSoup(partial_html, "html.parser")

    # Find all top-level elements in the partial HTML
    top_level_eles = partial_soup.find_all(recursive=False)

    for element in top_level_eles:
        soup.body.append(element)

    return soup.prettify()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="pick html file")
    args = parser.parse_args()
    html_content = clean_htm(args.source)
    print(html_content)
    print("number of token: ", count_token(html_content))


if __name__ == "__main__":
    main()
