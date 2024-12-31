from src.makeup.base_makeup import BaseMakeup
from src.utils.cv_helpers import create_mask
import cv2

class Eyeliner(BaseMakeup):
    def apply(self, src, landmarks):
        mask = create_mask(src, landmarks, self.color, thickness=self.thickness)
        return cv2.addWeighted(src, 1.0, mask, 0.6, 0.0)
