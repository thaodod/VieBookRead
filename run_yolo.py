import os
import os.path as osp
import cv2
import torch
import argparse
import json
from mmengine.config import Config
from mmengine.dataset import Compose
from mmdet.apis import init_detector
from mmdet.utils import get_test_pipeline_cfg
from torchvision.ops import nms
from PIL import Image, ImageDraw, ImageFont
import random

FONT = ImageFont.truetype("util/AlegreyaSans.ttf", 50)

def random_bright_color():
    """Generate a random bright color."""
    def random_component():
        return random.randint(100, 200)  # Ensure bright color

    return (random_component(), random_component(), random_component())

def draw_bounding_boxes(image_path, bounding_boxes):
    """Draw bounding boxes on the image."""
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    for box in bounding_boxes:
        color = random_bright_color()
        draw.rectangle(box['box'], outline=color, width=10)
        label = box['class'] + '/ ' + str(round(box['score'], 3))
        x = box['box'][0]
        y = box['box'][1]
        draw.text((x, y - 50), label, fill='green', font=FONT) # Adjust the position as needed

    return image

def parse_args():
    parser = argparse.ArgumentParser(description='Process images with a detector model.')
    parser.add_argument('--config-file', type=str, required=True, help='Path to the config file.')
    parser.add_argument('--checkpoint', type=str, required=True, help='Path to the checkpoint file.')
    parser.add_argument('--source-dir', type=str, required=True, help='Directory containing source images.')
    parser.add_argument('--csv-file', type=str, required=True, help='CSV file with image paths and flags.')
    parser.add_argument('--texts', type=str, required=True, help='Comma-separated list of texts.')
    parser.add_argument('--output-file', type=str, required=True, help='Output JSONL file for the results.')
    parser.add_argument('--score-thr', type=float, default=0.075, help='Score threshold for detections.')
    parser.add_argument('--max-dets', type=int, default=10, help='Maximum number of detections.')
    parser.add_argument('--output-dir', type=str, required=True, help='Output directory for copied images.')
    return parser.parse_args()

def filter_pred_instances(pred_instances, image_shape, texts, score_thr):
    image_area = image_shape[0] * image_shape[1]
    valid_mask = torch.ones(len(pred_instances), dtype=torch.bool, device=pred_instances.scores.device)

    for i, (box, label, score) in enumerate(zip(pred_instances.bboxes, pred_instances.labels, pred_instances.scores)):
        x1, y1, x2, y2 = box
        box_area = (x2 - x1) * (y2 - y1)
        label_text = texts[label.item()][0]
        
        current_score_thr = 0.18 if (label_text == 'stamp' or label_text == 'map') else score_thr
        
        if (x1 == 0.0 or y1 == 0.0 or x2 == 0.0 or y2 == 0.0 or
            box_area < 0.006 * image_area or box_area > 0.925 * image_area or
            score < current_score_thr):
            valid_mask[i] = False

    return pred_instances[valid_mask]

def inference(model, image, texts, test_pipeline, score_thr=0.075, max_dets=10):
    image = cv2.imread(image)
    image = image[:, :, [2, 1, 0]]
    data_info = dict(img=image, img_id=0, texts=texts)
    data_info = test_pipeline(data_info)
    data_batch = dict(
        inputs=data_info["inputs"].unsqueeze(0),
        data_samples=[data_info["data_samples"]],
    )
    with torch.no_grad():
        output = model.test_step(data_batch)[0]
    pred_instances = output.pred_instances
    
    keep = nms(pred_instances.bboxes,
               pred_instances.scores,
               iou_threshold=0.5)
    pred_instances = pred_instances[keep]
    
    if len(pred_instances.scores) > max_dets:
        indices = pred_instances.scores.float().topk(max_dets)[1]
        pred_instances = pred_instances[indices]

    pred_instances = filter_pred_instances(pred_instances, image.shape[:2], texts, score_thr)

    boxes = pred_instances.bboxes.cpu().numpy()
    labels = pred_instances.labels.cpu().numpy()
    scores = pred_instances.scores.cpu().numpy()
    label_texts = [texts[x][0] for x in labels]

    return boxes, labels, label_texts, scores

if __name__ == "__main__":
    args = parse_args()

    cfg = Config.fromfile(args.config_file)
    # init model
    cfg.load_from = args.checkpoint
    model = init_detector(cfg, checkpoint=args.checkpoint, device="cuda:0")
    test_pipeline_cfg = get_test_pipeline_cfg(cfg=cfg)
    test_pipeline_cfg[0].type = "mmdet.LoadImageFromNDArray"
    test_pipeline = Compose(test_pipeline_cfg)

    texts = [[text] for text in args.texts.split(",")] + [[' ']]

    import pandas as pd
    df = pd.read_csv(args.csv_file)
    
    with open(args.output_file, 'w') as f:
        for index, row in df.iterrows():
            image_path = osp.join(args.source_dir, row["filepath"])
            if row["result"].lower() in ["yes", "hard"]:
                print(f"starting to detect: {image_path}")
                boxes, labels, label_texts, scores = inference(
                    model, image_path, texts, test_pipeline, args.score_thr, args.max_dets
                )
                
                if len(boxes) > 0:  # If there are valid detections
                    results = {
                        "filepath": row["filepath"],
                        "detections": [
                            {
                                "class": f"{label_text}",
                                "box": box.tolist(),
                                "score": float(score)
                            }
                            for box, label_text, score in zip(boxes, label_texts, scores)
                        ]
                    }
                    
                    f.write(json.dumps(results) + '\n')
                    
                    # Copy and rename the image
                    flat_filename = row["filepath"].replace('/', '_')
                    dest_path = osp.join(args.output_dir, flat_filename)
                    os.makedirs(args.output_dir, exist_ok=True)
                    image = draw_bounding_boxes(image_path, results['detections'])
                    image.save(dest_path)
                    print(f"Drawed {image_path} to {dest_path}")

    print(f"Results saved to {args.output_file}")
    print(f"Images with detections copied to {args.output_dir}")
    
## python demo/run_yolo.py --config-file configs/pretrain/yolo_world_v2_x_vlpan_bn_2e-3_100e_4x8gpus_obj365v1_goldg_cc3mlite_train_lvis_minival.py --checkpoint weights/yolo_world_v2_x_obj365v1_goldg_cc3mlite_pretrain-8698fbfa.pth --source-dir ~/Viet123/data/page_input/ --csv-file ~/Viet123/data/group_check_fig/group-fig.csv --texts painting,map,stamp --output-file ~/Viet123/data/yolo6.jsonl --output-dir ~/Viet123/data/group_check_fig/yolo-o6