import cv2
from blocks import Block, EvenTracker, Tracker


class Blur(Block):
    def __init__(self, n=2, sigma=0):
        super().__init__()
        self.n, self.sigma = self.add_trackers(
            [
                EvenTracker("n", n, high=50),
                Tracker("sigma", sigma, high=50),
            ]
        )

    def operation(self):
        return cv2.GaussianBlur(
            self.input,
            (self.n.value, self.n.value),
            self.sigma.value,
            None,
            self.sigma.value,
        )
