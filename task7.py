import numpy as np
import cv2
from blocks import (
    ImageProcessor,
    Canny,
    FindContours,
    DrawContours,
    ChoseContour,
    MorphOpen,
    MorphClose,
)

original_image = cv2.imread("coin.jpg")
original_image = cv2.resize(
    original_image, np.array(original_image.shape[:2][::-1]) // 2
)
ImageProcessor(
    [
        Canny(82, 255),
        MorphClose(1),
        MorphOpen(0),
        FindContours(),
        ChoseContour(),
        DrawContours(original_image),
    ]
).apply(original_image)
