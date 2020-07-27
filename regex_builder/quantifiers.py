from .abc import Buildable
from abc import abstractmethod


class Quantifier(Buildable):
    def __init__(self, subject):
        self.subject = subject

    @abstractmethod
    def build(self):
        pass

class Optional(Quantifier):
    def build(self):
        return f"{self.subject}?"

class ZeroOrMore(Quantifier):
    def build(self):
        return f"{self.subject}*"

class OneOrMore(Quantifier):
    def build(self):
        return f"{self.subject}+"

class Exact(Quantifier):
    def __init__(self, subject, amount):
        super().__init__(subject)
        self.amount = amount

    def build(self):
        return f"{self.subject}{{self.amount}}"

class NOrMore(Quantifier):
    def __init__(self, subject, amount):
        super().__init__(subject)
        self.amount = amount

    def build(self):
        return f"{self.subject}{{{self.amount},}}"

class Between(Quantifier):
    def __init__(self, subject, min, max):
        super().__init__(subject)
        self.min = min
        self.max = max

    def build(self):
        return f"{self.subject}{{{self.min}, {self.max}}}"

