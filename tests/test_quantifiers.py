from regex_builder import Regex, Exact, Between, DIGIT

def test_exact():
    regex = (
        Regex()
        .section(Exact(DIGIT, 3))
    )

    assert regex.build() == r"\d{3}"


def test_between():
    regex = (
        Regex()
        .section(Between(DIGIT, 1, 5))
    )

    assert regex.build() == r"\d{1,5}"
