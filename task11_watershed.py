import cv2
from blocks import ImageProcessor, Watershed

original_image = cv2.imread("coins.png")
ImageProcessor([Watershed()]).apply(original_image)
