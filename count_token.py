import argparse
import tiktoken
from lxml.html.clean import Cleaner
from lxml.html import tostring, fromstring

# Initialize the tokenizer
tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")

def clean_class(html_content):
    html = fromstring(html_content)
    # Remove class attribute from all elements
    for tag in html.xpath("//*[@class]"):
        tag.attrib.pop("class")
    # Remove lang attribute from all elements
    for tag in html.xpath("//*[@lang]"):
        tag.attrib.pop("lang")
    
    return tostring(html, encoding="unicode", method="html")


def load_html_as_text(file_path):
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="pick html file")
    args = parser.parse_args()
    html_content = load_html_as_text(args.source)
    print("number of token: ", len(tokenizer.encode(html_content)))


if __name__ == "__main__":
    main()
