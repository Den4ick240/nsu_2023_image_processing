from blocks.Brightness import Brightness
import cv2
from blocks import (
    ImageProcessor,
    WrapAffine,
    WrapPerspective,
    BFMatcher,
)

original_image = cv2.imread("notredame.jpeg")
ImageProcessor(
    [
        Brightness(),
        WrapAffine(),
        WrapPerspective(),
        BFMatcher(original_image),
    ]
).apply(original_image)
