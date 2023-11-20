import cv2
from blocks import ImageProcessor, Drawer, GraphCut

for f in ["map1.png", "map2.png", "map3.png", "map4.png"]:
    original_image = cv2.imread(f)
    ImageProcessor(
        [
            Drawer(),
            Drawer(is_second=True),
            GraphCut(original_image),
        ]
    ).apply(original_image)
