import cv2
import numpy as np
from typing import Tuple

class ImagePreprocessor:
    def __init__(self, target_size: Tuple[int, int] = (640, 640)):
        self.target_size = target_size

    def preprocess(self, frame: np.ndarray) -> np.ndarray:
        resized = cv2.resize(frame, self.target_size)
        rgb_frame = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        return rgb_frame.astype(np.float32) / 255.0
