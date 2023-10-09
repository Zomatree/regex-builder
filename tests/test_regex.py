from regex_builder import Regex, Any, OneOrMore, DIGIT

def test_named_groups():
    regex = (
        Regex()
        .section(Any("A", "B", "C", name="letter"))
        .section("=")
        .section(Any(OneOrMore(DIGIT), name="number"))
    )

    assert regex.match("A=123").groupdict() == {"letter": "A", "number": "123"}
