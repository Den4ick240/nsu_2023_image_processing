import cv2
from blocks import ImageProcessor, Watershed


# for f in ["map1.png", "map2.png", "map3.png", "map4.png"]:
for f in ["coins.png"]:
    original_image = cv2.imread(f)
    ImageProcessor([Watershed()]).apply(original_image)
