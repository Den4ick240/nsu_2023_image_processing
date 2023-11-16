from blocks import Block, Tracker
import cv2


class Sobel(Block):
    def __init__(self, n=2):
        super().__init__()
        self.n = self.add_trackers(Tracker("n", n, high=5))

    def operation(self):
        gray = self.input
        x = cv2.Sobel(gray, self.n.value, 1, 0, ksize=3, scale=1)
        y = cv2.Sobel(gray, self.n.value, 0, 1, ksize=3, scale=1)
        absx = cv2.convertScaleAbs(x)
        absy = cv2.convertScaleAbs(y)
        edge = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)
        return edge
