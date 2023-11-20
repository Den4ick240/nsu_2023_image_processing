import cv2
from blocks import Block, Tracker


class RandN(Block):
    def __init__(self, mean=0, stddev=50):
        super().__init__()
        self.mean, self.stddev = self.add_trackers(
            [
                Tracker("mean", mean, high=500),
                Tracker("stddev", stddev, high=500),
            ]
        )

    def operation(self):
        return self.input + cv2.randn(
            self.input.copy(),
            (self.mean.value, self.mean.value, self.mean.value),
            (self.stddev.value, self.stddev.value, self.stddev.value),
        )
