from IPython.display import Image, display

import sys

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox


def detect_and_draw_box(filename, model="yolov3-tiny", confidence=0.5):
    """Detects common objects on an image and creates a new image with bounding boxes.

    Args:
        filename (str): Filename of the image.
        model (str): Either "yolov3" or "yolov3-tiny". Defaults to "yolov3-tiny".
        confidence (float, optional): Desired confidence level. Defaults to 0.5.
    """
    
    # Images are stored under the images/ directory
    img_filepath = f'/src/app/files/yolov/inputs_yolov/{filename}'
    
    # Read the image into a numpy array
    img = cv2.imread(img_filepath)
    
    # Perform the object detection
    bbox, label, conf = cv.detect_common_objects(img, confidence=confidence, model=model)
    
    # Print current image's filename
    print(f"========================\nImage processed: {filename}\n")
    
    # Print detected objects with confidence level
    for l, c in zip(label, conf):
        print(f"Detected object: {l} with confidence level of {c}\n")
    
    # Create a new image that includes the bounding boxes
    output_image = draw_bbox(img, bbox, label, conf)
    
    # Save the image in the directory images_with_boxes
    cv2.imwrite(f'/src/app/files/yolov/outputs_yolov/Output_{filename}', output_image)
    
    # Display the image with bounding boxes
    display(Image(f'/src/app/files/yolov/outputs_yolov/Output_{filename}'))

def video_detect_and_draw_box(filename):
    # out = cv2.VideoWriter(f'/src/app/files/yolov/outputs_yolov/Output_{filename}', -1, 20.0, (640,480))
    cv2.VideoWriter('filename.avi')
