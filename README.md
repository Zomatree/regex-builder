# Regex builder

programmatically make regex in python

## Simple example

```py
from regex_builder import Regex, Any


regex = (
    Regex()
    .section(Any("a", "b", "c"))
    .section("hello")
)

print(regex)
```
