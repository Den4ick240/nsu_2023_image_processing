import cv2
from blocks.MorphOperation import MorphOperation


class MorphClose(MorphOperation):
    def get_morph_operation(self):
        return cv2.MORPH_CLOSE
