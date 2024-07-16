import os
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz

def search_html_files(directory, query, threshold=80, block_size=4, padding=2):
    # List all HTML files in the directory
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    
    matching_files = []

    for html_file in html_files:
        # Read the content of the HTML file
        with open(os.path.join(directory, html_file), 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')
        paragraphs = soup.find_all(['p', 'div', 'span', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])  # Common tags containing text
        
        # Store the matching blocks with their scores and HTML
        matching_blocks = []
        
        # Calculate similarity scores for blocks of paragraphs
        for i in range(0, len(paragraphs), block_size):
            block = paragraphs[i:i + block_size]
            block_text = " ".join(paragraph.get_text() for paragraph in block)
            score = fuzz.partial_ratio(query, block_text)
            if score >= threshold:
                # Get the padded block
                start = max(0, i - padding)
                end = min(len(paragraphs), i + block_size + padding)
                padded_block = paragraphs[start:end]
                block_html = "".join(str(paragraph) for paragraph in padded_block)
                matching_blocks.append((block_html, score))
        
        if matching_blocks:
            # Calculate the average score for the document
            average_score = sum(score for _, score in matching_blocks) / len(matching_blocks)
            matching_files.append((html_file, average_score, matching_blocks))

    # Sort the matching files by their average score in descending order
    matching_files.sort(key=lambda x: x[1], reverse=True)

    return matching_files

# Example usage
directory = "data/html/003"
query = "Những sự phiêu dạt này tuy lam cho người Do-thai kho sở nhưng đồng thời lai luyện cho h8 có một đức-tính kiên-nhan rất"
matching_files = search_html_files(directory, query)

if matching_files:
    print("Ranked files containing text close to the query:")
    for file, score, blocks in matching_files:
        print(f"\nFile: {file}\nAverage Score: {score}")
        for block_html, b_score in blocks:
            print(f"Score: {b_score}\nHTML: {block_html}\n")
else:
    print("No matching files found.")
