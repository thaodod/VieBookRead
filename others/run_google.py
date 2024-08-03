import os
import json
import time
from google.cloud import documentai_v1 as documentai
from google.api_core.client_options import ClientOptions
import argparse
from pathlib import Path
from multiprocessing import Pool
import multiprocessing

# Replace with your Google Cloud project ID and location
PROJECT_ID = "***REMOVED***"
LOCATION = "us"
PROCESSOR_ID = "fa80821cbaf0aa18"

# Instantiates a client
docai_client = documentai.DocumentProcessorServiceClient(
    client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
)
RESOURCE_NAME = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)


def process_image(image_path, output_dir):
    """Processes a single image, extracts text, and creates a JSON file."""
    output_file = os.path.join(output_dir, Path(image_path).stem + ".json")
    if os.path.exists(output_file):
        # print(f"The file {output_file} already exists. Skip")
        return

    # Load image into memory
    with open(image_path, "rb") as image_file:
        image_content = image_file.read()

    # Load Binary Data into Document AI RawDocument Object
    raw_document = documentai.RawDocument(content=image_content, mime_type="image/jpeg")

    # Configure the process request
    request = documentai.ProcessRequest(name=RESOURCE_NAME, raw_document=raw_document)

    # Use the Document AI client to process the sample form
    result = docai_client.process_document(request=request)

    # Extract text from the document
    text = result.document.text

    # Save the JSON file

    with open(output_file, "w") as f:
        json.dump(text, f, indent=2, ensure_ascii=False)
    print(f"saved {output_file} successfully")
    time.sleep(0.2)


def process_file(args):
    image_path, output_dir = args
    try:
        process_image(image_path, output_dir)
    except Exception as e:
        return f"Error processing {image_path}: {str(e)}"
    return f"Successfully processed {image_path}"


def process_directory(input_dir, output_dir):
    tasks = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith((".jpg")):
                image_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_dir)
                file_output_dir = os.path.join(output_dir, relative_path)
                print(file_output_dir)
                os.makedirs(file_output_dir, exist_ok=True)
                tasks.append((image_path, file_output_dir))

    # Use all available CPU cores
    num_processes = int(multiprocessing.cpu_count() / 2)

    with Pool(processes=num_processes) as pool:
        results = pool.map(process_file, tasks)

    # Print results
    for result in results:
        print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process images and extract text")
    parser.add_argument("inp", type=str, help="Path to the input directory")
    parser.add_argument("out", type=str, help="Path to the output directory")
    args = parser.parse_args()

    process_directory(args.inp, args.out)
