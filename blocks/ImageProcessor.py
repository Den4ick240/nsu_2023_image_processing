from blocks.base import CompositeBlock
import cv2
import argparse
import re
import importlib


class Args:
    def __init__(self):
        self.current_image = None


class ImageProcessor(CompositeBlock):
    def __init__(self, blocks):
        super().__init__(blocks)
        self.keybinds = {
            ord("c"): self.read_and_execute_command,
            ord("q"): self.finish,
        }
        self.commands = {
            "remove": self.remove,
            "insert": self.insert_command,
            "exit": self.finish,
        }

    def apply(self, image, args=Args()):
        self.args = args
        self.set_image(image)

        cv2.imshow("original_image", self.input)

        self.init_self(args)

        try:
            self.not_finished = True
            while self.not_finished:
                fun = self.keybinds.get(cv2.waitKey())
                if fun is not None:
                    fun()
            self.remove_window()
        except Exception as e:
            raise e
        finally:
            cv2.destroyAllWindows()
        return self.res

    def read_and_execute_command(self):
        print("Blocks:")
        for block in self.blocks:
            print("    " + block.window_name())
        print("Waiting for command:")
        try:
            arguments = re.split(r" \s*(?![^()]*\))", input())
            self.cmd = get_parser().parse_args(arguments)
            self.commands.get(self.cmd.cmd)()
        except ArgumentParserError as e:
            print(e)

    def remove(self):
        print(f"removing {self.cmd.index}")
        del self[self.cmd.index]

    def insert_command(self):
        print(f"Inserting {self.cmd.item} at {self.cmd.index}")
        block = instantiate(self.cmd.item)
        self.blocks.insert(self.cmd.index, block)
        self.init_self()

    def finish(self):
        self.not_finished = False

    def set_image(self, image):
        self.args.current_image = image
        self.args.initial_image = image
        self.input = image.copy()

    def update_image(self, image):
        self.set_image(image)
        self.update()

    def init_self(self, args=None):
        if args is not None:
            self.args = args
        self.init(num="")
        self.args.global_update = self.update
        self.set_args(self.args)
        self.update()

    def update(self):
        self.remove_window()
        CompositeBlock.update(self)
        self.show_images()

    def __delitem__(self, index):
        self.blocks[index].remove_window()
        del self.blocks[index]
        self.init_self()


class ArgumentParserError(Exception):
    pass


class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)


def get_parser():
    parser = ThrowingArgumentParser("")
    subparsers = parser.add_subparsers(dest="cmd")
    insert = subparsers.add_parser("insert")
    insert.add_argument("index", type=int)
    insert.add_argument("item")
    remove = subparsers.add_parser("remove")
    remove.add_argument("index", type=int)
    subparsers.add_parser("exit")
    image = subparsers.add_parser("load")
    image.add_argument("course_name")
    image.add_argument("hole_index", type=int)
    subparsers.add_parser("next_image")
    return parser


def instantiate(class_name):
    module_name = f"green_detection.algorithms.blocks.{class_name}"
    module = importlib.import_module(module_name)
    _class = getattr(module, class_name)
    return _class()
