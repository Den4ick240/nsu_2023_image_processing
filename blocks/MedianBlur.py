import cv2
from blocks import Block, EvenTracker


class MedianBlur(Block):
    def __init__(self, n=2):
        super().__init__()
        self.n = self.add_trackers(EvenTracker("n", n, high=50))

    def operation(self):
        return cv2.medianBlur(self.input, self.n.value)
