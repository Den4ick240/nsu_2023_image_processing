import cv2
from blocks.ImageProcessor import ImageProcessor
from blocks.Blur import Blur
from blocks.Brightness import Brightness
from blocks.ShowHist import ShowHist
from blocks.EqualizeHist import EqualizeHist


ImageProcessor([Blur(), Brightness(), EqualizeHist(), ShowHist()]).apply(
    cv2.imread("image3.png", cv2.IMREAD_GRAYSCALE)
)
