import argparse
import json
import gc
from collections import defaultdict

from surya.detection import batch_text_detection
from surya.input.load import load_from_file
from surya.layout import batch_layout_detection
from surya.model.detection.segformer import load_model, load_processor
from surya.postprocessing.heatmap import draw_polys_on_image
from surya.settings import settings
import os


def process_batch(images, names, det_model, det_processor, model, processor):
    line_predictions = batch_text_detection(images, det_model, det_processor, batch_size=8)
    layout_predictions = batch_layout_detection(images, model, processor, line_predictions, batch_size=8)

    predictions_by_page = defaultdict(list)
    for idx, (pred, name, image) in enumerate(zip(layout_predictions, names, images)):
        out_pred = pred.model_dump(exclude=["segmentation_map"])
        out_pred["page"] = len(predictions_by_page[name]) + 1
        predictions_by_page[name].append(out_pred)

    return predictions_by_page


def main():
    parser = argparse.ArgumentParser(description="Detect layout of an input file or folder (PDFs or image).")
    parser.add_argument("input_path", type=str, help="Path to pdf or image file or folder to detect layout in.")
    parser.add_argument("--results_dir", type=str, help="Path to JSON file with layout results.", default=os.path.join(settings.RESULT_DIR, "surya"))
    parser.add_argument("--max", type=int, help="Maximum number of pages to process.", default=None)
    args = parser.parse_args()

    model = load_model(checkpoint=settings.LAYOUT_MODEL_CHECKPOINT)
    processor = load_processor(checkpoint=settings.LAYOUT_MODEL_CHECKPOINT)
    det_model = load_model()
    det_processor = load_processor()

    result_path = os.path.join(args.results_dir, os.path.basename(args.input_path).split(".")[0])
    os.makedirs(result_path, exist_ok=True)

    all_predictions = defaultdict(list)

    if os.path.isdir(args.input_path):
        image_files = [os.path.join(args.input_path, fname) for fname in os.listdir(args.input_path) if fname.lower().endswith(('.jpg'))]
    else:
        image_files = [args.input_path]

    batch_size = 50  # Adjust batch size according to your memory constraints
    for i in range(0, len(image_files), batch_size):
        batch_files = image_files[i:i + batch_size]
        batch_images = []
        batch_names = []
        for file in batch_files:
            images, names = load_from_file(file, 1)
            batch_images.extend(images)
            batch_names.extend(names)

        batch_predictions = process_batch(batch_images, batch_names, det_model, det_processor, model, processor)
        for name, preds in batch_predictions.items():
            all_predictions[name].extend(preds)

        # Explicitly delete objects and call garbage collector
        del batch_images, batch_names, batch_predictions
        gc.collect()

    with open(os.path.join(result_path, "results.json"), "w+", encoding="utf-8") as f:
        json.dump(all_predictions, f, ensure_ascii=False)

    print(f"Wrote results to {result_path}")


if __name__ == "__main__":
    main()
