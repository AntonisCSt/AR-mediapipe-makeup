import cv2
import numpy as np

def create_mask(src, points, color, thickness=-1):
    mask = np.zeros_like(src)
    if thickness == -1:
        mask = cv2.fillPoly(mask, [points], color)
    else:
        mask = cv2.polylines(mask, [points], isClosed=False, color=color, thickness=thickness)
    return cv2.GaussianBlur(mask, (7, 7), 5)
