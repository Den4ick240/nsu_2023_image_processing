from blocks import Block, Tracker
import cv2


class WrapAffine(Block):
    def __init__(self, angle=0, scale=1, tx=0, ty=0):
        super().__init__()
        self.angle, self.scale, self.tx, self.ty = self.add_trackers(
            [
                Tracker("angle", angle, high=360),
                Tracker("scale", scale, high=10),
                Tracker("tx", tx, high=100),
                Tracker("ty", ty, high=100),
            ]
        )

    def operation(self):
        rows, cols = self.input.shape[:2]
        M = cv2.getRotationMatrix2D(
            (cols / 2, rows / 2),
            self.angle.value,
            self.scale.value,
        )
        M[0, 2] += self.tx.value
        M[1, 2] += self.ty.value
        return cv2.warpAffine(
            self.input,
            M,
            (cols, rows),
        )
