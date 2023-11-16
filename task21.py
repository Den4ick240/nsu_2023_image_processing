import cv2

img = cv2.imread("image2.png", cv2.IMREAD_GRAYSCALE)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)
images = [
    ["Original", img],
    ["Default threshold", th1],
    ["Adaptive mean", th2],
    ["Adaptive gaussian", th3],
]

for name, img in images:
    cv2.imshow(name, img)

while cv2.waitKey() != ord("q"):
    pass

cv2.destroyAllWindows()
