import cv2
from blocks.base import Block


class EqualizeHist(Block):
    def operation(self):
        return cv2.equalizeHist(self.input)
