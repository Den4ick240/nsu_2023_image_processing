import cv2
import numpy as np
from blocks import Block, Tracker


class HoughLines(Block):
    def __init__(self, original_image):
        super().__init__()
        self.original_image = original_image
        (
            self.param1,
            self.param2,
            self.minRadius,
            self.maxRadius,
            self.dp,
            self.minDst,
        ) = self.add_trackers(
            [
                Tracker("param1", 50, high=100),
                Tracker("param2", 30, high=100),
                Tracker("minRadius", 10, high=100),
                Tracker("maxRadius", 100, high=100),
                Tracker("dp", 1, high=100),
                Tracker("minDst", 20, high=100),
            ]
        )

    def operation(self):
        circles = cv2.HoughCircles(
            self.input,
            cv2.HOUGH_GRADIENT,
            self.dp.value,
            self.minDst.value,
            param1=self.param1.value,
            param2=self.param2.value,
            minRadius=self.minRadius.value,
            maxRadius=self.maxRadius.value,
        )
        img = self.original_image.copy()
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
        return img
