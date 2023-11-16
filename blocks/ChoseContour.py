from blocks import Block, Tracker


class ChoseContour(Block):
    def __init__(self, index=0):
        super().__init__()
        self.index = self.add_trackers(Tracker("index", index, high=500))

    def operation(self):
        return self.input[0], self.input[1][self.index.value : self.index.value + 1]
