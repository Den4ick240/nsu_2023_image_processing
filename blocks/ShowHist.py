import numpy as np
import cv2
from blocks import Block


class ShowHist(Block):
    def operation(self):
        img = self.input
        bins = np.arange(256).reshape(256, 1)
        h = np.zeros((300, 256, 3))
        # color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        color = [(255, 0, 0)]
        for ch, col in enumerate(color):
            hist_item = cv2.calcHist([img], [ch], None, [256], [0, 255])
            cv2.normalize(hist_item, hist_item, 0, 255, cv2.NORM_MINMAX)
            hist = np.int32(np.around(hist_item))
            pts = np.column_stack((bins, hist))
            cv2.polylines(h, [pts], False, col)

            h = np.flipud(h)
            return h
