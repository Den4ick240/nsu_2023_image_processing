import cv2
import numpy as np
from sklearn.datasets import load_digits


class KNN:
    def __init__(self, n_neighbors):
        self.n_neighbors = n_neighbors

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def _predict(self, x):
        distances = [np.linalg.norm(x - x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[: self.n_neighbors]
        k_nearest_labels = self.y_train[k_indices]
        most_common = np.bincount(k_nearest_labels).argmax()
        return most_common


def get_predictor():
    mnist = load_digits()
    x = mnist.data
    y = mnist.target
    model = KNN(3)
    model.fit(x, y)
    return model._predict


drawing = False  # true if mouse is pressed
pt1_x, pt1_y = None, None

th = 12


# mouse callback function
def line_drawing(event, x, y, flags, param):
    global pt1_x, pt1_y, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pt1_x, pt1_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img, (pt1_x, pt1_y), (x, y), color=(255, 255, 255), thickness=th)
            pt1_x, pt1_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (pt1_x, pt1_y), (x, y), color=(255, 255, 255), thickness=th)


n = 128
img = np.zeros((n, n, 1), np.uint8)
cv2.namedWindow("test draw")
cv2.setMouseCallback("test draw", line_drawing)

predict = get_predictor()
while 1:
    cv2.imshow("test draw", img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("c"):
        img = np.zeros((n, n, 1), np.uint8)
    elif key == ord("p"):
        res = cv2.resize(img, (8, 8))
        cv2.imshow("res", res)
        print(predict(res.reshape(-1)))
cv2.destroyAllWindows()
