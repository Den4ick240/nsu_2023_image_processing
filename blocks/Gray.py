from blocks import Block
import cv2


class Gray(Block):
    def operation(self):
        return cv2.cvtColor(self.input, cv2.COLOR_BGR2GRAY)
