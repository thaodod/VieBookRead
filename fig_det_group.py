import pandas as pd
import argparse


def clean_answer(answer):
    answer = answer.strip().lower()
    if answer.startswith("yes"):
        return "yes"
    else:
        return "no"


def final_answer(row):
    if row["answer_file1"] == "no" and row["answer_file2"] == "no":
        return "no"
    else:
        return "yes"


def process_files(file1_path, file2_path, output_path):
    # Load the CSV files
    file1 = pd.read_csv(file1_path)
    file2 = pd.read_csv(file2_path)

    # Apply the cleaning function to the second file
    file2["answer"] = file2["answer"].apply(clean_answer)

    # Merge the two files on the filepath column
    merged = file1.merge(file2, on="filepath", suffixes=("_file1", "_file2"))

    # Apply the final answer function
    merged["answer"] = merged.apply(final_answer, axis=1)

    # Select the required columns for the output
    output = merged[["filepath", "answer"]]

    # Save the output to a new CSV file
    output.to_csv(output_path, index=False)

    print(f"The output CSV file has been saved as '{output_path}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process and compare 2 CSV files.")
    parser.add_argument("--file1", type=str, required=True, help="Path to surya csv")
    parser.add_argument("--file2", type=str, required=True, help="Path to DocOwl csv")
    parser.add_argument(
        "--out", type=str, required=True, help="Path to output CSV file"
    )

    args = parser.parse_args()

    process_files(args.file1, args.file2, args.out)
