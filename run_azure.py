import time
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.exceptions import HttpResponseError

import json
import os

def process_image(input_path, output_path, document_analysis_client):
    try:
        with open(input_path, "rb") as f:
            poller = document_analysis_client.begin_analyze_document(
                "prebuilt-read", analyze_request=f, content_type="image/jpg")

        analyze_result = poller.result()
        result_json = analyze_result.as_dict()

        with open(output_path, 'w', encoding='utf8') as f:
            json.dump(result_json, f, ensure_ascii=False, indent=4)
        
        return True  # Successfully processed the image

    except HttpResponseError:
        return False  # Encountered the specific Azure error

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return False  # Any other unexpected error

def process_directory(input_dir, output_dir, document_analysis_client):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith('.jpg'):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + '.json')
                
                # Check if output JSON already exists
                if os.path.exists(output_path):
                    print(f"Skipping {input_path} - Output already exists")
                    continue
                
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                print(f"Processing: {input_path}")
                success = process_image(input_path, output_path, document_analysis_client)
                if success:
                    print(f"Output saved to: {output_path}")
                else:
                    print(f"Failed to process: {input_path}")
                    time.sleep(120)
                    process_directory(input_dir, output_dir, document_analysis_client)
                    
                    

def main():
    # Your Azure Form Recognizer endpoint and API key
    endpoint = "https://viet121.cognitiveservices.azure.com/"
    key = "***REMOVED***"
    credential = AzureKeyCredential(key)
    document_analysis_client = DocumentIntelligenceClient(endpoint, credential)

    # Set your input and output directories
    input_directory = "D:/DATA/page_input"
    output_directory = "D:/DATA/output_json"

    process_directory(input_directory, output_directory, document_analysis_client)

if __name__ == "__main__":
    main()