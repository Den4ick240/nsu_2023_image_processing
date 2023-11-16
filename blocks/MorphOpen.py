import cv2
from blocks.MorphOperation import MorphOperation


class MorphOpen(MorphOperation):
    def get_morph_operation(self):
        return cv2.MORPH_OPEN
