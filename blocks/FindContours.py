import cv2
from blocks import Block


class FindContours(Block):
    def operation(self):
        contours, hierarchy = cv2.findContours(
            self.input, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        return self.input, contours, hierarchy
