from .abc import Buildable
from .section import Section
from .errors import NotSection
from re import match


class Regex(Buildable):
    def __init__(self):
        self.sections = []

    def build(self):
        return "".join(map(str, self.sections))

    def group(self, regex):
        self.sections.append(regex)

    def section(self, section):
        if not (issubclass(type(section), Buildable) or isinstance(section, str)):
            raise NotSection(f"{section} is not a subclass of Buildable")
        self.sections.append(section)
        return self

    def match(self, string):
        return match(self.build(), string)
