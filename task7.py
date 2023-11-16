import cv2
from blocks import (
    ImageProcessor,
    Canny,
    FindContours,
    DrawContours,
)

original_image = cv2.imread("cards.png")
ImageProcessor(
    [
        Canny(),
        FindContours(),
        DrawContours(original_image),
    ]
).apply(original_image)
