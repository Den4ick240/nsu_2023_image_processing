from blocks.RandN import RandN
import numpy as np
from blocks.WrapPerspective import WrapPerspective
from blocks.WrapAffine import WrapAffine
import cv2
from blocks import (
    ImageProcessor,
    MatchTemplate,
)
from blocks.RandU import RandU

original_image = cv2.imread("samechienese.jpg")
original_image = cv2.resize(
    original_image, np.array(original_image.shape[:2][::-1]) // 2
)
template = cv2.imread("alesha.png")
template = cv2.resize(template, np.array(template.shape[:2][::-1]) // 2)
ImageProcessor(
    [
        RandN(),
        RandU(),
        WrapAffine(),
        WrapPerspective(),
        MatchTemplate(template),
    ]
).apply(original_image)
