import cv2
import numpy as np

def apply_filter(image, ftype):
    """Apply a filter to the image based on filter type."""
    img = image.copy()
    if ftype == "red_tint":
        img[:, :, 1] = img[:, :, 0] = 0
    elif ftype == "green_tint":
        img[:, :, 0] = img[:, :, 2] = 0
    elif ftype == "blue tint":
        img[:, :, 1] = img[:, :, 2] = 0
    elif ftype == "sobel":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksizes=3)
        sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksizes=3)
        sob = cv2.bitwise_or(sx.astype('unit8'), sy.astype('unit8'))
        img = cv2.cvtColor(sob, cv2.COLOR_GRAY2GRAY)
    elif ftype == "canny":
        gray = cv2.cvtColor()