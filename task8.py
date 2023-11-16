import cv2
from blocks import ImageProcessor, Blur, Gray, HoughLines

original_image = cv2.imread("lines.png")
ImageProcessor(
    [
        Blur(),
        Gray(),
        HoughLines(original_image),
    ]
).apply(original_image)
