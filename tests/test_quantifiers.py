import re
from regex_builder import Regex, Exact, DIGIT

def test_exact():
    regex = (
        Regex()
            .section(Exact(DIGIT, 3))
    )

    assert regex.build() == r"\d{3}"
