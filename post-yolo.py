import json
import os
import shutil
from typing import List, Dict
import numpy as np

def iou(box1, box2):
    """Compute Intersection over Union (IoU) of two boxes."""
    x1, y1, x2, y2 = box1
    x1g, y1g, x2g, y2g = box2
    
    xi1 = max(x1, x1g)
    yi1 = max(y1, y1g)
    xi2 = min(x2, x2g)
    yi2 = min(y2, y2g)
    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)
    
    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x2g - x1g) * (y2g - y1g)
    
    union_area = box1_area + box2_area - inter_area
    
    return inter_area / union_area if union_area != 0 else 0

def is_fully_covered(inner_box, outer_box):
    """Check if inner_box is fully covered by outer_box."""
    x1, y1, x2, y2 = inner_box
    x1g, y1g, x2g, y2g = outer_box
    
    return x1 >= x1g and y1 >= y1g and x2 <= x2g and y2 <= y2g

def load_jsonl(filepath: str) -> List[Dict]:
    with open(filepath, 'r') as file:
        return [json.loads(line) for line in file]

def save_jsonl(data: List[Dict], filepath: str):
    with open(filepath, 'w') as file:
        for item in data:
            json.dump(item, file)
            file.write('\n')

def flatten_path(filepath: str) -> str:
    return filepath.replace(os.sep, '_')

def main(root_dir: str, lp_jsonl: str, yolo_jsonl: str, output_pruned: str, output_only_lp: str, only_lp_dir: str):
    lp_data = load_jsonl(lp_jsonl)
    yolo_data = load_jsonl(yolo_jsonl)
    
    yolo_dict = {item['filepath']: item['detections'] for item in yolo_data}
    pruned_yolo = []
    only_lp = []

    if not os.path.exists(only_lp_dir):
        os.makedirs(only_lp_dir)

    for lp_item in lp_data:
        filepath = lp_item['filepath']
        lp_boxes = lp_item['figures']
        
        if filepath in yolo_dict:
            yolo_boxes = yolo_dict[filepath]
            if lp_boxes:
                lp_box = lp_boxes[0]
                iou_scores = [iou(lp_box, yolo_box['box']) for yolo_box in yolo_boxes]
                
                if any(score > 0 for score in iou_scores):
                    max_iou_index = np.argmax(iou_scores)
                    pruned_boxes = [yolo_boxes[max_iou_index]]
                    pruned_boxes.extend([yolo_box for iou_score, yolo_box in zip(iou_scores, yolo_boxes) if iou_score == 0])
                else:
                    pruned_boxes = yolo_boxes
            else:
                pruned_boxes = []
                yolo_boxes.sort(key=lambda x: x['score'], reverse=True)
                for i, box in enumerate(yolo_boxes):
                    if not any(is_fully_covered(box['box'], other['box']) for other in yolo_boxes[i+1:]):
                        pruned_boxes.append(box)
            
            pruned_yolo.append({
                'filepath': filepath,
                'detections': pruned_boxes
            })
        else:
            if lp_boxes:
                only_lp.append(lp_item)
                flattened_filename = flatten_path(filepath)
                shutil.copy(os.path.join(root_dir, filepath), os.path.join(only_lp_dir, flattened_filename))
    
    save_jsonl(pruned_yolo, output_pruned)
    save_jsonl(only_lp, output_only_lp)

# Parameters
root_dir = 'data/page_input/'
lp_jsonl = 'data/lp-o.jsonl'
yolo_jsonl = 'data/yolo.jsonl'
output_pruned = 'data/yolo_pruned.jsonl'
output_only_lp = 'data/only_lp.jsonl'
only_lp_dir = 'data/lp_only'

main(root_dir, lp_jsonl, yolo_jsonl, output_pruned, output_only_lp, only_lp_dir)
