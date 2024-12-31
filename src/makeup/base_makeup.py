import numpy as np
import cv2

class BaseMakeup:
    def __init__(self, color: str, thickness: int = -1):
        self.color = color
        self.thickness = thickness

    def apply(self, src, landmarks):
        raise NotImplementedError("This method should be implemented by subclasses.")
