import numpy as np
import cv2
from blocks import Block
from blocks.trackers import FloatTracker, Tracker, EvenTracker


class HarrisCorners(Block):
    def __init__(self):
        super().__init__()
        (self.block_size, self.ksize, self.k, self.threshold) = self.add_trackers(
            [
                Tracker("block_size", 2, high=20),
                EvenTracker("ksize", 3, high=10),
                FloatTracker("k", 0.04, 0.5, 0.01),
                FloatTracker("threshold", 0.01, 0.2, 0.001),
            ]
        )

    def operation(self):
        image = self.input
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect Harris corners
        gray = np.float32(gray)
        dst = cv2.cornerHarris(
            gray,
            self.block_size.value,
            self.ksize.value,
            self.k.value,
        )  # Adjust parameters for your specific image

        # Dilate to mark the corners
        dst = cv2.dilate(dst, None)

        # Threshold the image to keep only important corners
        threshold = self.threshold.value * dst.max()
        corner_image = image.copy()
        corner_image[dst > threshold] = [0, 0, 255]  # Red color for corners
        return image, corner_image

    def image_to_show(self):
        return self.res[1]
