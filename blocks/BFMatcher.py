import cv2
from blocks import Block, Tracker


class BFMatcher(Block):
    def __init__(self, original_image):
        super().__init__()
        self.original_image = original_image
        self.num_matches_drawn = self.add_trackers(
            Tracker("num_matches_drawn", 10, high=100)
        )

    def operation(self):
        img1 = self.original_image
        img2 = self.input
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)

        return cv2.drawMatches(
            img1,
            kp1,
            img2,
            kp2,
            matches[: self.num_matches_drawn.value],
            None,
            flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
        )
