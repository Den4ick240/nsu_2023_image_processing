import cv2
import numpy as np
from blocks import Block, Tracker


class ChoseContour(Block):
    def __init__(self, index=0):
        super().__init__()
        self.index = self.add_trackers(Tracker("index", index, high=500))

    def operation(self):
        selected_contour = self.input[1][self.index.value : self.index.value + 1]
        self.selected_contour = (
            selected_contour[0] if len(selected_contour) > 0 else None
        )

        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10, 500)
        bottomLeftCornerOfText2 = (10, 300)
        fontScale = 1
        fontColor = (255, 255, 255)
        thickness = 1
        lineType = 2
        img = self.input[0].copy() * 0
        shape = classify_shape(self.selected_contour)
        cv2.putText(
            img,
            "Taken area: {0:.2g}%".format(self.get_area_persent()),
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            thickness,
            lineType,
        )
        cv2.putText(
            img,
            shape,
            bottomLeftCornerOfText2,
            font,
            fontScale,
            fontColor,
            thickness,
            lineType,
        )
        return img, selected_contour

    def get_area_persent(self):
        hull = cv2.convexHull(self.selected_contour)
        area = cv2.contourArea(hull)
        height, width = self.input[0].shape[:2]
        img_area = height * width
        return area / img_area * 100.0


def get_center(contour):
    # Calculate moments of the contour
    M = cv2.moments(contour)
    center_x = int(M["m10"] / M["m00"])
    center_y = int(M["m01"] / M["m00"])
    return (center_x, center_y)


def get_distance(point1, point2):
    return np.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def classify_shape(contour):
    center = get_center(contour)
    distances = [get_distance(point[0], center) for point in contour]
    max_distance_points = sorted(
        contour, key=lambda point: get_distance(point[0], center), reverse=True
    )[:4]

    distances_from_center = [
        get_distance(point[0], center) for point in max_distance_points
    ]
    distances_from_center.sort()

    if all(abs(dist - distances_from_center[0]) < 5 for dist in distances):
        return "Circle"
    elif len(max_distance_points) == 4:
        side_lengths = [
            get_distance(max_distance_points[i][0], max_distance_points[(i + 1) % 4][0])
            for i in range(4)
        ]
        if all(abs(length - side_lengths[0]) < 5 for length in side_lengths):
            return "Square"
        else:
            return "Rectangle"
    else:
        return "Triangle"
