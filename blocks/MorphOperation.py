import cv2
from blocks import Block, EvenTracker
import numpy as np


class MorphOperation(Block):
    def __init__(self, kernel_size=3, morph_operation=None):
        super().__init__()
        if morph_operation is None:
            morph_operation = self.get_morph_operation()
        self.morph_operation = morph_operation
        self.kernel_size = self.add_trackers(
            EvenTracker("kernel size", kernel_size, 35)
        )

    def operation(self):
        return cv2.morphologyEx(
            self.input,
            self.morph_operation,
            np.ones((self.kernel_size.value, self.kernel_size.value), np.uint8),
        )

    def get_morph_operation(self):
        return None
