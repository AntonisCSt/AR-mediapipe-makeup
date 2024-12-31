from src.makeup.base_makeup import BaseMakeup
from src.utils.cv_helpers import create_mask
import cv2

class Lipstick(BaseMakeup):
    def apply(self, src, landmarks):
        lip_mask = create_mask(src, landmarks, self.color)
        return cv2.addWeighted(src, 1.0, lip_mask, 0.4, 0.0)
