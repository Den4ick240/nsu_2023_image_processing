import cv2
from blocks import Block, ImageProcessor, MatchTemplate
from task12_mnist import get_predictor

predictor = get_predictor()


def match_template(img, templ):
    res = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_val


class DotaCutter(Block):
    def __init__(self, original_image, img):
        super().__init__()
        # self.original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        self.original_image = original_image
        self.img = img

    def operation(self):
        _, _, (top, bottom, left, right) = self.input
        left, right = right, right + 30
        top, bottom = top + 6, bottom - 8
        img = self.original_image[top:bottom, left:right]
        width = img.shape[1]
        quarter = width // 4
        img1 = img[::, :quarter]
        img2 = img[::, quarter : quarter * 2]
        img3 = img[::, quarter * 2 + 1 : quarter * 3 + 1]
        img4 = img[::, quarter * 3 + 1 : -2]
        # cv2.imwrite("1" + self.img, img1)
        # cv2.imwrite("2" + self.img, img2)
        # cv2.imwrite("3" + self.img, img3)
        # cv2.imwrite("4" + self.img, img4)
        print(
            get_digit(img1),
            get_digit(img2),
            get_digit(img3),
            get_digit(img4),
        )

        return img1, None, self.input[2]


def get_digit(img):
    md = 0
    mv = 0
    for digit, template in enumerate(
        [
            "0.jpg",
            "1.jpg",
            "2.jpg",
            "3.jpg",
            "4.jpg",
            "5.jpg",
            "6.jpg",
            "7.jpg",
            "8.jpg",
            "9.jpg",
        ]
    ):
        v = match_template(img, cv2.imread(template))
        if v > mv:
            mv = v
            md = digit

    return md


# 3908
# 3100
# 4232
# 2716
# 3954
# 3813

template = cv2.imread("dota_template.png")
for original_image_name in [
    "dota1.jpg",
    "dota2.jpg",
    "dota3.jpg",
    "dota4.jpg",
    "dota5.jpg",
    "dota6.jpg",
    "dota11.jpg",
]:
    original_image = cv2.imread(original_image_name)
    ImageProcessor(
        [
            MatchTemplate(template),
            DotaCutter(original_image, original_image_name),
        ]
    ).apply(original_image)
