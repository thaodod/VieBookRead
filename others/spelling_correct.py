# Compare with Hierarchical Transformer Encoders for Vietnamese Spelling Correction
# by VNG Zalo team
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
import time
import json
import os
import argparse
import glob
import multiprocessing as mp


class SpellingChecker:
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")

        # Specify the path to your downloaded geckodriver
        geckodriver_path = "/home/thao/Viet123/others/geckodriver"
        service = FirefoxService(executable_path=geckodriver_path)

        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.get("https://nlp.laban.vn/wiki/spelling_checker/")

    def check_spelling(self, text):
        try:
            # Wait for the input text area to be present
            input_area = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "input_text"))
            )

            # Clear the existing text and input the new text
            input_area.clear()
            input_area.send_keys(text)

            # Find and click the check button
            check_button = self.driver.find_element(By.ID, "btnCheckSpelling")
            check_button.click()

            # Wait for the results to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "divSugesstedResult"))
            )

            # Give a short pause to ensure all results are loaded
            time.sleep(1)

            # Get the suggested result
            suggested_result = self.driver.find_element(
                By.ID, "divSugesstedResult"
            ).text

            # Get the model info
            model_info = self.driver.find_element(By.ID, "divModelInfo").text

            return {"suggested_result": suggested_result, "model_info": model_info}

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def close(self):
        self.driver.quit()


def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data[1:]
    except json.JSONDecodeError:
        print(f"Error: '{file_path}' is not a valid JSON")
        return None


def process_json(args, js_path):
    checker = SpellingChecker()
    js_basename = os.path.basename(js_path)
    save_target = os.path.join(args.o, js_basename)

    # Skip if output file already exists
    if os.path.exists(save_target):
        print(f"Skipping {js_basename} as output already exists.")
        return

    para_list = load_json(js_path)
    out_list = []

    try:
        for para in para_list:
            para_text = para["content"]
            if len(para_text.strip()) < 2:
                continue

            max_retries = 5
            retry_delay = 5  # seconds

            for attempt in range(max_retries):
                try:
                    result = checker.check_spelling(para_text)
                    if result:
                        out_list.append(result["suggested_result"])
                    else:
                        print(f"Failed to fix spelling for: {para_text}")
                    break  # Success, exit retry loop
                except Exception as e:
                    if attempt < max_retries - 1:
                        print(
                            f"Error processing paragraph: {e}. Retrying in {retry_delay} seconds..."
                        )
                        time.sleep(retry_delay)
                    else:
                        print(
                            f"Failed to process paragraph after {max_retries} attempts: {para_text}"
                        )

            time.sleep(0.5)
    finally:
        checker.close()

    if not os.path.exists(args.o):
        os.makedirs(args.o, exist_ok=True)

    with open(save_target, "w", encoding="utf-8") as file:
        json.dump(out_list, file, indent=2, ensure_ascii=False)
    print(f"Saved file {save_target} successfully")


def main():
    parser = argparse.ArgumentParser(description="correct spelling by VNG")
    parser.add_argument("json_dir", help="dir to load input clean json files")
    parser.add_argument("o", help="where to save json files of a book")

    args = parser.parse_args()

    json_paths = glob.glob(os.path.join(args.json_dir, "*.json"))

    # Use multiprocessing to process JSON files in parallel
    with mp.Pool(processes=3) as pool:
        pool.starmap(
            process_json,
            [(args, in_js_path) for in_js_path in json_paths],
        )


if __name__ == "__main__":
    main()
