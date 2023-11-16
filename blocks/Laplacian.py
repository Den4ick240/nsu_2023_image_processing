from blocks import Block
import cv2


class Laplacian(Block):
    def operation(self):
        return cv2.Laplacian(self.input, cv2.CV_64F)
