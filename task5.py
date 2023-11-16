import cv2
from blocks import (
    Blur,
    MedianBlur,
    RandN,
    ImageProcessor,
    RandU,
    Filter2d,
    Sobel,
    Gray,
    Laplacian,
)

ImageProcessor(
    [RandN(), RandU(), Blur(), MedianBlur(), Filter2d(), Gray(), Sobel(), Laplacian()]
).apply(cv2.imread("lena.png"))
