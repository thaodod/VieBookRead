import pandas as pd
import argparse

# Function to calculate IoU (Intersection over Union)
def calculate_iou(box1, box2):
    x1, y1, x2, y2 = box1
    x3, y3, x4, y4 = box2
    
    xi1 = max(x1, x3)
    yi1 = max(y1, y3)
    xi2 = min(x2, x4)
    yi2 = min(y2, y4)
    
    inter_area = max(0, xi2 - xi1 + 1) * max(0, yi2 - yi1 + 1)
    
    box1_area = (x2 - x1 + 1) * (y2 - y1 + 1)
    box2_area = (x4 - x3 + 1) * (y4 - y3 + 1)
    
    union_area = box1_area + box2_area - inter_area
    
    iou = inter_area / union_area
    
    return iou

# Function to check if box1 is fully overlapped by box2
def is_fully_overlapped(box1, box2):
    x1, y1, x2, y2 = box1
    x3, y3, x4, y4 = box2
    
    return x1 >= x3 and y1 >= y3 and x2 <= x4 and y2 <= y4

def process_boxes(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Convert box strings to numerical lists
    df['box'] = df['box'].apply(lambda x: list(map(float, x.strip('[]').split())))

    # Initialize a column to mark ignored boxes
    df['ignored'] = False

    # Process each image
    for filepath in df['filepath'].unique():
        image_df = df[df['filepath'] == filepath]
        for i, row1 in image_df.iterrows():
            if df.at[i, 'ignored']:
                continue
            box1 = row1['box']
            score1 = float(row1['score'].split('-')[1])
            for j, row2 in image_df.iterrows():
                if i == j or df.at[j, 'ignored']:
                    continue
                box2 = row2['box']
                score2 = float(row2['score'].split('-')[1])
                
                # Check for full overlap
                if is_fully_overlapped(box1, box2):
                    df.at[i if score1 < score2 else j, 'ignored'] = True
                # Check for high IoU
                elif calculate_iou(box1, box2) >= 0.8:
                    df.at[i if score1 < score2 else j, 'ignored'] = True

    # Filter out ignored boxes
    filtered_df = df[~df['ignored']]

    # Drop the 'ignored' column
    filtered_df = filtered_df.drop(columns=['ignored'])

    # Save the result to a new CSV file
    filtered_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process bounding boxes in CSV file.")
    parser.add_argument('--input', type=str, help='Path to the input CSV file')
    parser.add_argument('--output', type=str, help='Path to the output CSV file')
    
    args = parser.parse_args()
    
    process_boxes(args.input, args.output)
