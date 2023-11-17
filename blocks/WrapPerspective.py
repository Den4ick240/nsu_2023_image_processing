import numpy as np
import cv2
from blocks import Block, Tracker, FloatTracker


class WrapPerspective(Block):
    def __init__(self, angle=0, scale=1, tx=0, ty=0):
        super().__init__()
        (
            self.x1,
            self.x2,
            self.x3,
            self.x4,
            self.y1,
            self.y2,
            self.y3,
            self.y4,
        ) = self.add_trackers(
            [
                FloatTracker("x1", 0, 1, 0.01),
                FloatTracker("x2", 1, 1, 0.01),
                FloatTracker("x3", 0, 1, 0.01),
                FloatTracker("x4", 1, 1, 0.01),
                FloatTracker("y1", 0, 1, 0.01),
                FloatTracker("y2", 0, 1, 0.01),
                FloatTracker("y3", 1, 1, 0.01),
                FloatTracker("y4", 1, 1, 0.01),
            ]
        )

    def operation(self):
        rows, cols = self.input.shape[:2]

        original_pts = np.float32(
            [[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]]
        )
        new_pts = np.float32(
            [
                [self.x1.value * cols, self.y1.value * rows],
                [self.x2.value * cols, self.y2.value * rows],
                [self.x3.value * cols, self.y3.value * rows],
                [self.x4.value * cols, self.y4.value * rows],
            ]
        )

        M = cv2.getPerspectiveTransform(original_pts, new_pts)

        return cv2.warpPerspective(
            self.input,
            M.astype(np.float32),
            (cols, rows),
        )
