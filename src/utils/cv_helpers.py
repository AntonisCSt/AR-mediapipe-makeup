import cv2
import numpy as np

def create_mask(src, points, color, thickness=-1):
    """
    Create a mask with the specified points and color.

    Args:
        src (np.ndarray): Source image.
        points (list): List of points for the mask.
        color (list): Color of the mask.
        thickness (int): Thickness of the line (-1 for filled).

    Returns:
        np.ndarray: Mask with the specified points drawn.
    """
    mask = np.zeros_like(src)

    # Convert points to the correct shape (n, 1, 2) for OpenCV
    points = np.array(points, dtype=np.int32).reshape((-1, 1, 2))

    if thickness == -1:
        mask = cv2.fillPoly(mask, [points], color)
    else:
        mask = cv2.polylines(mask, [points], isClosed=False, color=color, thickness=thickness)

    return cv2.GaussianBlur(mask, (7, 7), 5)

