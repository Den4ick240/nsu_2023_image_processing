import numpy as np
import cv2
from blocks import Block, Tracker


class Filter2d(Block):
    def operation(self):
        kernel2 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        return cv2.filter2D(src=self.input, ddepth=-1, kernel=kernel2)
