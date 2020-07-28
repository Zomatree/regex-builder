from .abc import Buildable
from abc import abstractmethod


class Escaped(Buildable):
    def __init__(self, target):
        self.target = target

    def build(self):
        return f"\\{self.target}"