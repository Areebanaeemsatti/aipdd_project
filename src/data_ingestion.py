import cv2
import numpy as np
from typing import Tuple, Optional

class DataIngestion:
    def __init__(self, stream_url: str):
        self.stream_url = stream_url
        self.cap: Optional[cv2.VideoCapture] = None

    def connect_stream(self) -> bool:
        self.cap = cv2.VideoCapture(self.stream_url)
        return self.cap.isOpened()

    def read_frame(self) -> Tuple[bool, Optional[np.ndarray]]:
        if self.cap is None or not self.cap.isOpened():
            return False, None
        return self.cap.read()
