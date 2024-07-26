import time
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.exceptions import HttpResponseError

import json
import os
import argparse


def process_image(input_path, output_path, document_analysis_client, m="r"):
    if m == "r":
        m = "prebuilt-read"
    else:
        m = "prebuilt-layout"
    try:
        with open(input_path, "rb") as f:
            poller = document_analysis_client.begin_analyze_document(
                m, analyze_request=f, content_type="image/jpg"
            )

        analyze_result = poller.result()
        result_json = analyze_result.as_dict()

        with open(output_path, "w", encoding="utf8") as f:
            json.dump(result_json, f, ensure_ascii=False, indent=4)

        return True  # Successfully processed the image

    except HttpResponseError:
        return False  # Encountered the specific Azure error

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return False  # Any other unexpected error


def process_directory(input_dir, output_dir, d_a_client, m):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(".jpg"):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(
                    output_dir, os.path.splitext(relative_path)[0] + ".json"
                )

                # Check if output JSON already exists
                if os.path.exists(output_path):
                    print(f"Skipping {input_path} - Output already exists")
                    continue

                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                print(f"Processing: {input_path}")
                success = process_image(input_path, output_path, d_a_client, m)
                if success:
                    print(f"Output saved to: {output_path}")
                else:
                    print(f"Failed to process: {input_path}")
                    time.sleep(30)
                    process_directory(input_dir, output_dir, d_a_client)


def main():
    parser = argparse.ArgumentParser(description="run azure da")
    parser.add_argument("source", help="dir to load all images")
    parser.add_argument("o", help="where to save json files")
    parser.add_argument("-m", default="r", help="mode: read or layout")

    args = parser.parse_args()
    # Your Azure Form Recognizer endpoint and API key
    endpoint = "https://viet121.cognitiveservices.azure.com/"
    key = "***REMOVED***"
    credential = AzureKeyCredential(key)
    d_a_client = DocumentIntelligenceClient(endpoint, credential)

    # Set your input and output directories
    inp_dir = args.source
    out_dir = args.o

    process_directory(inp_dir, out_dir, d_a_client, m=args.m)


if __name__ == "__main__":
    main()
