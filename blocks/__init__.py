from blocks.base import Block, CompositeBlock
from blocks.trackers import (
    Tracker,
    EvenTracker,
    PercentTracker,
)
import os
import sys

path = os.path.dirname(os.path.abspath(__file__))

for py in [
    f[:-3] for f in os.listdir(path) if f.endswith(".py") and f != "__init__.py"
]:
    mod = __import__(".".join([__name__, py]), fromlist=[py])
    classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
    for cls in classes:
        setattr(sys.modules[__name__], cls.__name__, cls)


__all__ = ["Block", "CompositeBlock", "Tracker", "EvenTracker", "PercentTracker"]
