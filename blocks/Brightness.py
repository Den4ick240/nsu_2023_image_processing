import cv2
from blocks import Block
from blocks.trackers import Tracker, FloatTracker


class Brightness(Block):
    def __init__(self):
        super().__init__()
        self.alpha, self.beta, self.gamma = self.add_trackers(
            [
                Tracker("alpha", 125, high=255),
                Tracker("beta", 0, high=255),
                FloatTracker("gamma", 1, high=5, step=0.01),
            ]
        )

    def operation(self):
        img = self.input
        res_img = img.copy()
        height, width = img.shape
        for y in range(height):
            for x in range(width):
                # for ch in range(1):
                res_px = self.alpha.value * img[y, x] / 125 + self.beta.value
                res_px = min(255, res_px)
                res_px = (res_px / 255) ** self.gamma.value * 255
                res_img[y, x] = min(255, res_px)
        return res_img
