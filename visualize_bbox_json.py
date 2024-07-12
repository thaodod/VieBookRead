import jsonlines
from PIL import Image, ImageDraw, ImageFont
import random
import os

IMAGE_DIR  = 'data/page_input'
SAVER_IMAGE_DIR = 'data/yolo-final'

font = ImageFont.truetype("util/AlegreyaSans.ttf", 50)


def random_bright_color():
    """Generate a random bright color."""
    def random_component():
        return random.randint(100, 200)  # Ensure component is above 100 for brightness

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
        draw.text((x, y - 50), label, fill='purple', font=font) # Adjust the position as needed

    return image

def process_jsonl(file_path):
    """Process the JSONL file to read image paths and bounding boxes."""
    with jsonlines.open(file_path) as reader:
        for obj in reader:
            re_image_path = obj['filepath']
            image_path = os.path.join(IMAGE_DIR, re_image_path)
            bounding_boxes = obj['detections']
            image = draw_bounding_boxes(image_path, bounding_boxes)
            os.makedirs(SAVER_IMAGE_DIR, exist_ok=True)
            save_img_path = os.path.join(SAVER_IMAGE_DIR, re_image_path.split('/')[0] + re_image_path.split('/')[1])

            image.save(save_img_path)
            # image.show()  # Display the image with bounding boxes

if __name__ == "__main__":
    jsonl_file_path = 'data/yolo-final.jsonl'  # Update with the path to your JSONL file
    process_jsonl(jsonl_file_path)
