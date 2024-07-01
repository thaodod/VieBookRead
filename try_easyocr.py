# -*- coding: utf-8 -*-
"""
Change to conda env surya!
"""

import cv2
import easyocr
import matplotlib.pyplot as plt

#img_url = './test4_with_EN_FR.png'
img_url = './test1.jpg'
reader = easyocr.Reader(['vi', 'en']) # this needs to run only once
text_detections = reader.readtext(img_url, paragraph=True)
img = cv2.imread(img_url)

def draw_bounding_boxes(image, detections, threshold=0.25):
    for bbox, text in detections:
        cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 5)
        #cv2.putText(image, text, tuple(map(int, bbox[0])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255, 0, 0), 2)
            

draw_bounding_boxes(img, text_detections)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGBA))
plt.show()