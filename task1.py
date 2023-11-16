import cv2

img = cv2.imread("image.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = img.shape[:2]
print("Input brightness:")
brightness = int(input())
print("Counting...")
count = 0
for x in range(width):
    for y in range(height):
        if img[y, x] >= brightness:
            count += 1


all_pixels = height * width
print(f"All pixels count: {all_pixels}")
print(f"Pixels brighter than: {brightness}")
print(f"Count={count}")
print(f"Percent={100.0 * count / all_pixels}")

cv2.imshow("Window name", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
