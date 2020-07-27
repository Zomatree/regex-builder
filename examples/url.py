from regex_builder import Regex, ANY_CHAR, OneOrMore


regex = (
    Regex()
    .section(OneOrMore(ANY_CHAR))
    .section("\\@")
    .section(OneOrMore(ANY_CHAR))
    .section("\\.")
    .section(OneOrMore(ANY_CHAR))
)

print(regex)
print(regex.match("a@b.com"))
