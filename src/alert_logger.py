import logging
from typing import Dict, Any

class AlertLogger:
    def __init__(self, log_file: str = "logs/attendance.log"):
        logging.basicConfig(filename=log_file, level=logging.INFO)

    def log_attendance(self, student_id: str, confidence: float) -> bool:
        logging.info(f"Student: {student_id} | Conf: {confidence}")
        return True
