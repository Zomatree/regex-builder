from .abc import Buildable
from abc import abstractmethod


class Section(Buildable):
    def __init__(self, parts):
        self.parts = parts

    @abstractmethod
    def build(self):
        pass


class Any(Section):
    def __init__(self, *parts, capture=True, name=None):
        if not capture and name:
            raise Exception("Cant specify group name and not capture")
        if name == "":
            raise Exception("Name cannot be an empty string")

        super().__init__(parts)
        self.capture = capture
        self.name = name


    def build(self):
        # parts can be Sections so we string them to call section.build
        parts = "|".join(map(str, self.parts))
        capture = "" if self.capture else "?:"
        name = f"?<{self.name}>" if self.name else ""
        return f"({capture}{name}{parts})"

