from regex_builder import Regex, ANY_CHAR, OneOrMore, Escaped


regex = (
    Regex()
    .section(OneOrMore(ANY_CHAR))
    .section(Escaped("@"))
    .section(OneOrMore(ANY_CHAR))
    .section(Escaped("."))
    .section(OneOrMore(ANY_CHAR))
)

print(regex)
print(regex.match("a@b.com"))
