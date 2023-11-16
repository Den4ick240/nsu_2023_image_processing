class Tracker:
    def __init__(self, name, value, high):
        self.value = None
        self.on_change(value)
        self.name = name
        self.high = high

    def on_change(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __iter__(self):
        yield self.name
        yield self.get_value()
        yield self.high
        yield self.on_change


class BooleanTracker(Tracker):
    def __init__(self, name, value: bool):
        self.value = value

        super().__init__(name + "_false/true", self.get_value(), 1)

    def on_change(self, value):
        self.value = value == 1

    def get_value(self):
        if self.value:
            return 1
        else:
            return 0


class PercentTracker(Tracker):
    def __init__(self, name, value, high=100):
        super().__init__(name, value, high)

    def on_change(self, value):
        self.value = value / 100.0

    def get_value(self):
        return int(self.value * 100)


class EvenTracker(Tracker):
    def on_change(self, value):
        self.value = value * 2 + 1

    def get_value(self):
        return int((self.value - 1) / 2)


class FloatTracker(Tracker):
    def __init__(self, name, value, high, step):
        self.step = step
        self.value = value
        super().__init__(name, self.get_value(), int(high / step))

    def get_value(self):
        return int(self.value / self.step)

    def on_change(self, value):
        self.value = value * self.step
