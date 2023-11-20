import cv2
from blocks import Block, Tracker, FloatTracker
import numpy as np


class ShiTomachi(Block):
    def __init__(self):
        super().__init__()
        (
            self.maxCorners,
            self.qualityLevel,
            self.minDistance,
        ) = self.add_trackers(
            [
                Tracker("maxCorners", 100, high=500),
                FloatTracker("qualityLevel", 0.01, 0.2, 0.01),
                Tracker("minDistance", 10, high=100),
            ]
        )

    def operation(self):
        image = self.input[0]
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(
            gray, self.maxCorners.value, self.qualityLevel.value, self.minDistance.value
        )
        corners = np.int0(corners)
        crn_image = image.copy()
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(crn_image, (x, y), 5, (0, 255, 0), -1)
        return image, crn_image

    def image_to_show(self):
        return self.res[1]
