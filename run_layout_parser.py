import argparse
import cv2
import layoutparser as lp

def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Layout parsing with user-specified input image")
    parser.add_argument("--input", type=str, required=True,
                        help="Path to the input image file")
    parser.add_argument("--model", type=str, default='publay')
    args = parser.parse_args()
    return args

def main():
    """Main function for layout parsing."""
    args = parse_arguments()

    # Load the image based on the input argument
    image = cv2.imread(args.input)
    image = image[..., ::-1]

    # Define the layout parsing model
    if args.model == 'publay':
        model = lp.Detectron2LayoutModel('lp://PubLayNet/mask_rcnn_X_101_32x8d_FPN_3x',
                                        extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8],
                                        label_map={0: "Text", 1: "Title", 2: "List", 3: "Table", 4: "Figure"})
    else:
        model = lp.Detectron2LayoutModel('lp://TableBank/faster_rcnn_R_101_FPN_3x/config',
                                        extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8],
                                        label_map={0: "Table"})

    # Define the color mapping for visualization
    color_map = {"Text": 'green', "Title": 'red', "List": 'white', "Table": 'black', "Figure": 'blue'}

    # Perform layout detection and visualization
    layout = model.detect(image)
    lp.draw_box(image, layout, box_width=3, show_element_id=True, color_map=color_map).show()

if __name__ == "__main__":
    main()
