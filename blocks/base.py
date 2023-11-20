import cv2
import numpy as np


class Block:
    def __init__(self):
        self.args = None
        self.num = 0
        self.next_block = None
        self.input = None
        self.trackbar_created = False
        self.trackers = []
        self.res = None
        self.isOn = True
        self.name = self.__class__.__name__

    def disable(self):
        self.isOn = False
        return self

    def add_trackers(self, tracker):
        if type(tracker) is list:
            return map(self.add_trackers, tracker)
        else:
            self.trackers.append(tracker)
            return tracker

    def remove_window(self):
        if self.trackbar_created:
            cv2.destroyWindow(self.window_name())
        self.trackbar_created = False

    def init(self, num, next_block=None):
        self.remove_window()
        self.num = num
        self.next_block = next_block

    def set_args(self, args):
        self.args = args

    def update(self):
        if self.isOn:
            self.res = self.operation()
        else:
            self.res = self.off_operation()
        if self.next_block is not None:
            self.next_block.input = self.res
            self.next_block.update()

    def show_images(self):
        image = self.image_to_show()
        if image is None:
            return
        cv2.imshow(self.window_name(), image)
        if not self.trackbar_created:
            self.create_trackbars()
            self.trackbar_created = True

    def image_to_show(self):
        if not isinstance(self.res, np.ndarray) and self.res is not None:
            return self.res[0]
        return self.res

    def create_trackbars(self):
        for name, value, high, setter in self.trackers + [
            ("on/off", 1 if self.isOn else 0, 1, self.set_on_off)
        ]:
            cv2.createTrackbar(
                name, self.window_name(), value, high, self.get_on_change(setter)
            )

    def set_on_off(self, value):
        self.isOn = value > 0

    def get_on_change(self, setter):
        def f(value):
            setter(value)
            if self.trackbar_created:
                self.update()
                self.show_images_recur()

        return f

    def show_images_recur(self):
        self.show_images()
        if self.next_block is not None:
            self.next_block.show_images_recur()

    def operation(self):
        pass

    def off_operation(self):
        return self.input

    def window_name(self):
        return f"Step {self.num} {self.name}"


class CompositeBlock(Block):
    def __init__(self, blocks):
        super().__init__()
        self.blocks = blocks

    def set_args(self, args):
        self.args = args
        for block in self.blocks:
            block.set_args(args)

    def update(self):
        first_step = self.blocks[0]
        first_step.input = self.input
        first_step.update()
        self.res = self.blocks[-1].res

    def init(self, num, next_block=None):
        self.next_block = None
        for i, block in enumerate(self.blocks):
            if i + 1 < len(self.blocks):
                next_block_inner = self.blocks[i + 1]
            else:
                next_block_inner = next_block
            block.init(f"{num}_{i}", next_block_inner)

    def show_images(self):
        for block in self.blocks:
            block.show_images()

    def remove_window(self):
        for block in self.blocks:
            block.remove_window()


class ForkInnerNext:
    def __init__(self, parent):
        self.parent = parent

    def update(self):
        self.parent.on_update()


# class Fork(Block):
#     def __init__(self, block1, block2):
#         super().__init__()
#         self.block1 = block1
#         self.block2 = block2
#         self.next = ForkInnerNext()
#
#     def remove_window(self):
#         self.block1.remove_window()
#         self.block2.remove_window()
#
#     def init(self, num, next_block=None):
#         self.block1.init("1 + " + num, self.next)
#         self.block2.init("2 + " + num, self.next)
#         self.num = num
#         self.next_block = next_block
#
#     def set_args(self, args):
#         self.args = args
#         self.block1.set_args(args)
#         self.block2.set_args(args)
#
#     def show_images(self):
#         super().show_images(self)
#         self.block1.show_images()
#         self.block2.show_images()
#
#     def update(self):
#         if self.isOn:
#             self.res = self.operation()
#         else:
#             self.res = self.off_operation()
#         if self.next_block is not None:
#             self.next_block.input = self.res
#             self.next_block.update()
#
#     def image_to_show(self):
#         return np.zeros((1, 1, 1))
#
#     def show_images_recur(self):
#         self.show_images()
#         if self.next_block is not None:
#             self.next_block.show_images_recur()
#
#     def operation(self):
#         pass
#
#     def off_operation(self):
#         return self.input
#
#     def window_name(self):
#         return f"Step {self.num} {self.name}"
