import cv2
from blocks import Block


class DrawContours(Block):
    def __init__(self, orig_image):
        super().__init__()
        self.orig_image = orig_image

    def operation(self):
        contours = self.input[1]
        return cv2.drawContours(self.orig_image.copy(), contours, -1, (0, 0, 255), 2)
