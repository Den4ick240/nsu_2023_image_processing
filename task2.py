import numpy as np
import cv2

global img
img = cv2.imread("kotey.png")

ear1 = [[65, 11], [121, 58], [138, 99], [95, 95], [50, 150]]

ear2 = [
    [273, 68],
    [358, 10],
    [368, 74],
    [342, 139],
    [322, 79],
]

eye1center = [154, 202]
eye2center = [271, 200]

nose = [
    [183, 262],
    [215, 238],
    [237, 257],
    [212, 288],
]


def draw(arr, isClosed=True, color=(255, 0, 0)):
    global img
    pts = np.array(arr, np.int32)
    pts = pts.reshape((-1, 1, 2))
    thickness = 2
    img = cv2.polylines(img, [pts], isClosed, color, thickness)


cv2.ellipse(img, np.array([70, 90], np.int32), [30, 80], 0, 135, 270, (255, 255, 0), 2)
draw(ear1, isClosed=False)
draw(ear2)
cv2.fillPoly(img, pts=[np.array(nose, np.int32)], color=(0, 255, 0))
cv2.circle(img, eye1center, 20, (0, 0, 255), 2)
cv2.circle(img, eye2center, 20, (0, 0, 255), 2)

cv2.imshow("kotey", img)
while cv2.waitKey() != ord("q"):
    pass

cv2.destroyAllWindows()
