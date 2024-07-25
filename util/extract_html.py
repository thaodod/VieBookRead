from bs4 import BeautifulSoup, NavigableString, Tag
import re


def clean_nested_spans(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    def should_unwrap(tag):
        return tag.name in ["div", "span"] and (
            not tag.attrs or (len(tag.attrs) == 1 and "class" in tag.attrs)
        )

    def recursive_unwrap(element):
        if isinstance(element, Tag):
            children = list(element.children)
            for child in children:
                recursive_unwrap(child)
            if should_unwrap(element):
                element.unwrap()

    recursive_unwrap(soup)

    # Remove empty tags
    for tag in soup.find_all():
        if len(tag.get_text(strip=True)) == 0:
            tag.extract()

    return str(soup)


def flatten_html(html_content):
    cleaned_html = clean_nested_spans(html_content)
    soup = BeautifulSoup(cleaned_html, "html.parser")

    paragraphs = []
    current_paragraph = []

    stack = [soup.body or soup]

    while stack:
        element = stack.pop()

        if isinstance(element, NavigableString):
            current_paragraph.append(str(element))
        elif isinstance(element, Tag):
            # Remove nested <a> around <sub>/<sup> or <sub>/<sup> around <a>
            if (
                element.name == "a"
                and any(child.name in ["sub", "sup"] for child in element.children)
            ) or (
                element.name in ["sub", "sup"]
                and any(child.name == "a" for child in element.children)
            ):
                continue
            elif element.name in ["br", "p", "div", "li", "aside"]:
                if current_paragraph:
                    paragraphs.append("".join(current_paragraph))
                    current_paragraph.clear()
                if element.name != "br":
                    for child in reversed(element.contents):
                        stack.append(child)
            else:
                if element.name in [
                    "a",
                    "sub",
                    "sup",
                    "h1",
                    "h2",
                    "h3",
                    "h4",
                    "h5",
                    "h6",
                ]:
                    current_paragraph.append(element.get_text())
                else:
                    for child in reversed(element.contents):
                        stack.append(child)

    if current_paragraph:
        paragraphs.append("".join(current_paragraph))

    # Filter out empty or all-space paragraphs, wrap with <p> tags
    cleaned_paragraphs = []
    for p in paragraphs:
        if p.strip():
            # Clean up whitespace
            cleaned = re.sub(r"\s+", " ", p.strip())
            cleaned_paragraphs.append(f"<p>{cleaned}</p>")

    return cleaned_paragraphs
