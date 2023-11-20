import cv2
from blocks import Block


class MatchTemplate(Block):
    def __init__(self, template_image):
        super().__init__()
        self.template_image = template_image

    def operation(self):
        res = cv2.matchTemplate(self.input, self.template_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        h, w = self.template_image.shape[:2]
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        img = self.input.copy()
        cv2.rectangle(img, top_left, bottom_right, 255, 2)
        return res, img

    def show_images(self):
        cv2.imshow(self.window_name() + "rect", self.res[1])
        return super().show_images()
