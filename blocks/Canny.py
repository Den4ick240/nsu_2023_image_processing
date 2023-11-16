import cv2
from blocks import Block, Tracker


class Canny(Block):
    def __init__(self, low=40, high=100):
        super().__init__()
        self.low, self.high = self.add_trackers(
            [
                Tracker("low", low, high=255),
                Tracker("high", high, high=255),
            ]
        )

    def operation(self):
        return cv2.Canny(
            self.input,
            min(self.low.value, self.high.value),
            max(self.low.value, self.high.value),
        )
