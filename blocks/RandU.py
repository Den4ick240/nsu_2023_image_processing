import cv2
from blocks import Block, Tracker


class RandU(Block):
    def __init__(self, mean=0, stddev=50):
        super().__init__()
        self.mean, self.stddev = self.add_trackers(
            [
                Tracker("mean", mean, high=255),
                Tracker("stddev", stddev, high=255),
            ]
        )

    def operation(self):
        return self.input + cv2.randu(
            self.input.copy(),
            (self.mean.value, self.mean.value, self.mean.value),
            (self.stddev.value, self.stddev.value, self.stddev.value),
        )
