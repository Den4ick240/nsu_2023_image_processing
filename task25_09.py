import random
import cv2

img = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("orig", img)
n = 50
nosy = []
height, width = img.shape[:2]
for i in range(30):
    nos = img.copy()
    for y in range(height):
        for x in range(width):
            nos[y, x] = min(255, max(0, nos[y, x] + random.randint(-n, n)))
    nosy.append(nos)

for i in range(min(len(nosy), 4)):
    cv2.imshow(f"nosy{i}", nosy[i])

res = img.copy()
for y in range(height):
    for x in range(width):
        res[y, x] = min(255, max(0, sum([n[y, x] for n in nosy]) / len(nosy)))

cv2.imshow("res", res)

print(nosy[0][0][0])
print(nosy[1][0][0])

while cv2.waitKey() != ord("q"):
    pass

cv2.destroyAllWindows()
