from regex_builder import Regex, Any


regex = (
    Regex()
    .section(Any("a", "b", "c", Any("1", "2")))
    .section("hello")
)

print(regex)
