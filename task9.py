from blocks.Brightness import Brightness
import cv2
from blocks import (
    ImageProcessor,
    HarrisCorners,
    ShiTomachi,
    WrapAffine,
    WrapPerspective,
)

original_image = cv2.imread("notredame.jpeg")
ImageProcessor(
    [
        Brightness(),
        WrapAffine(),
        WrapPerspective(),
        HarrisCorners(),
        ShiTomachi(),
    ]
).apply(original_image)
