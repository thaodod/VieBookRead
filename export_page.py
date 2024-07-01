import fitz  # PyMuPDF
import os
import csv
from PIL import Image
import io

RESOL = 216

def extract_images_from_pdfs(pdf_dir, output_base_dir, csv_path):
    # Read the CSV file
    page_ranges = {}
    with open(csv_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            pdf_id, start_page, end_page = map(int, row)
            page_ranges[pdf_id] = (start_page, end_page)
    
    # Process each PDF in the directory
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            pdf_id = int(filename[:3])
            pdf_path = os.path.join(pdf_dir, filename)
            output_dir = os.path.join(output_base_dir, f"{pdf_id:03d}")
            
            if pdf_id in page_ranges:
                start_page, end_page = page_ranges[pdf_id]
                extract_images(pdf_path, output_dir, start_page, end_page)
            else:
                print(f"Skipping {filename}: No page range specified in CSV")

def extract_images(pdf_path, output_dir, start_page, end_page):
    doc = fitz.open(pdf_path)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for page_num in range(start_page - 1, end_page):  # Adjust for 0-based index
        if page_num < len(doc):
            page = doc[page_num]
            
            # Set the resolution to 360 DPI
            zoom = RESOL / 72  # 72 is the default DPI for PDF
            mat = fitz.Matrix(zoom, zoom)
            
            # Render page to an image
            pix = page.get_pixmap(matrix=mat)
            
            # Convert to PIL Image
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            output_filename = f"page_{page_num + 1}.jpg"
            output_path = os.path.join(output_dir, output_filename)
            
            # Save as high quality JPEG
            img.save(output_path, "JPEG", quality=95)
            
            print(f"Exported page {page_num + 1} from {os.path.basename(pdf_path)}: {output_filename}")
    
    doc.close()
    print(f"Page export complete for {os.path.basename(pdf_path)}")

# Usage
pdf_dir = "D:\DATA\input"
output_base_dir = "D:\DATA\page_input"
csv_path = "D:\DATA\start_end.csv"
extract_images_from_pdfs(pdf_dir, output_base_dir, csv_path)