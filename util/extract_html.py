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
    # First, clean up the nested structure
    cleaned_html = clean_nested_spans(html_content)
    soup = BeautifulSoup(cleaned_html, "html.parser")

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    paragraphs = []
    current_paragraph = []

    def process_element(element):
        if isinstance(element, NavigableString):
            current_paragraph.append(str(element))
        elif isinstance(element, Tag):
            if element.name in ["br", "p", "div", "li"] or element.name in [
                "h1",
                "h2",
                "h3",
                "h4",
                "h5",
                "h6",
            ]:
                if current_paragraph:
                    paragraphs.append("".join(current_paragraph))
                    current_paragraph.clear()
                if element.name != "br":
                    if element.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                        current_paragraph.append(f"<{element.name}>")
                    for child in element.children:
                        process_element(child)
                    if element.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                        current_paragraph.append(f"</{element.name}>")
            elif element.name in ["sup", "sub", "a"]:
                current_paragraph.append(str(element))
            else:
                for child in element.children:
                    process_element(child)

    # Handle cases where there might not be a body tag or when the body is empty
    body = soup.body or soup
    if body:
        for element in body.children:
            process_element(element)

    if current_paragraph:
        paragraphs.append("".join(current_paragraph))

    # Filter out empty or all-space paragraphs, wrap with <p> tags, and clean up whitespace
    cleaned_paragraphs = []
    for p in paragraphs:
        if p.strip():
            # Clean up whitespace
            cleaned = re.sub(r"\s+", " ", p.strip())
            cleaned_paragraphs.append(f"<div>{cleaned}</div>")

    return cleaned_paragraphs
