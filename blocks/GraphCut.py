import cv2
import numpy as np
from blocks import Block
from blocks.trackers import Tracker


class GraphCut(Block):
    def __init__(self, original_image):
        super().__init__()
        self.original_image = original_image
        (self.left, self.right, self.top, self.bottom) = self.add_trackers(
            [
                Tracker("left", 0, 1000),
                Tracker("right", 100, 1000),
                Tracker("top", 0, 1000),
                Tracker("bottom", 100, 1000),
            ]
        )

    def operation(self):
        _, sure_bg, sure_fg = self.input
        img = self.original_image
        mask = sure_fg.copy() * 0 + 2
        mask[sure_fg == 255] = 1
        mask[sure_bg == 0] = 0
        try:
            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)
            rect = (
                self.left.value,
                self.top.value,
                self.right.value,
                self.bottom.value,
            )
            # rect = None
            cv2.grabCut(
                img,
                mask,
                rect,
                bgdModel,
                fgdModel,
                2,
                cv2.GC_INIT_WITH_MASK,
            )
            mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
            img = img * mask2[:, :, np.newaxis]
            rect = (
                self.left.value,
                self.top.value,
                self.right.value - self.left.value,
                self.bottom.value - self.top.value,
            )
            cv2.rectangle(img, rect, (255, 0, 0), 2)
            return img
        except Exception as e:
            print(e)
            return self.input[0]
