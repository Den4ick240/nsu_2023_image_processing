from blocks import MorphOpen
from blocks import MorphClose
import cv2
from blocks import (
    ImageProcessor,
    Canny,
    FindContours,
    DrawContours,
    ChoseContour,
)

original_image = cv2.imread("cards.png")
ImageProcessor(
    [
        Canny(82, 255),
        MorphClose(),
        MorphOpen(),
        FindContours(),
        ChoseContour(),
        DrawContours(original_image),
    ]
).apply(original_image)
