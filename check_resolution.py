import os
from PIL import Image

def check_large_images(directory):
    # Loop through all subdirectories and files in the given directory
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file is an image based on common extensions
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tif', '.tiff')):
                # Construct the full file path
                filepath = os.path.join(subdir, file)
                try:
                    # Open the image
                    with Image.open(filepath) as img:
                        width, height = img.size
                        # Check if either dimension is greater than 10,000
                        if width > 10000 or height > 10000:
                            print(f"Large image found: {filepath} (Width: {width}, Height: {height})")
                except Exception as e:
                    print(f"Failed to open image {filepath}. Reason: {e}")

# Replace 'path_to_your_directory' with the path to the directory you want to check
check_large_images('D:\DATA\page_input')
