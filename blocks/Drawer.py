import cv2
from blocks import Block
from blocks.trackers import BooleanTracker


class Drawer(Block):
    def __init__(self, is_second=False):
        super().__init__()
        self.drawing = False
        self.pt1_x = None
        self.pt1_y = None
        self.drawing_image = None
        self.is_second = is_second
        if is_second:
            self.color = (255, 255, 255)
        else:
            self.color = (0, 0, 0)

        (self.clear,) = self.add_trackers([BooleanTracker("clear", False)])

    def line_drawing(self, event, x, y, _, __):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.pt1_x, self.pt1_y = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                cv2.line(
                    self.drawing_image,
                    (self.pt1_x, self.pt1_y),
                    (x, y),
                    color=self.color,
                    thickness=6,
                )
                self.pt1_x, self.pt1_y = x, y
                self.res = self.operation()
                self.show_images()
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            cv2.line(
                self.drawing_image,
                (self.pt1_x, self.pt1_y),
                (x, y),
                color=self.color,
                thickness=6,
            )

            self.update()
            self.show_images_recur()

    def show_images(self):
        super().show_images()
        cv2.setMouseCallback(self.window_name(), self.line_drawing)

    def operation(self):
        if self.is_second:
            img = self.input[0]
        else:
            img = self.input.copy()

        if (
            self.drawing_image is None
            or self.drawing_image.shape != img.shape
            or self.clear.value
        ):
            self.drawing_image = img.copy() * 0
            if self.color[0] == 0:
                self.drawing_image += 255

        res = img.copy()
        res[self.drawing_image == self.color] = self.color[0]
        draw_res = cv2.cvtColor(self.drawing_image, cv2.COLOR_BGR2GRAY)
        if self.is_second:
            return res, self.input[1], draw_res
        return res, draw_res

    def image_to_show(self):
        return self.res[0]
