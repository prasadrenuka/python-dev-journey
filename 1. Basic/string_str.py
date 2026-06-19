# single quote
a= 'renuka'
# double quote
b= "prasad"
# overriding the variable  b value
b ='p'


print(b)
# example of dynamically calling variable in print
print(f"{a} {b}")

print(len(a))
print(f"python string has {len(dir(str))} methods and methods are \n{dir(str)}")

# Notes
'''
object: a value stored in memory with a type
function: a block of code you call to do something
print() is both function (print value) and object because it has type
Note: Everything in python is an object

dir () print's out all the attributes and methods available on an object
'''
# Categorizing string methods based on use cases
categories = {
    "Case Conversion": [
        "capitalize", "lower", "upper", "title", "swapcase", "casefold"
    ],
    "Search & Check": [
        "find", "rfind", "index", "rindex", "startswith", "endswith", "count"
    ],
    "Validation / Checks (is...)": [
        "isalnum", "isalpha", "isascii", "isdecimal", "isdigit", "isidentifier",
        "islower", "isnumeric", "isprintable", "isspace", "istitle", "isupper"
    ],
    "Modification": [
        "replace", "strip", "lstrip", "rstrip", "removeprefix", "removesuffix",
        "center", "ljust", "rjust", "zfill", "expandtabs", "translate"
    ],
    "Splitting & Joining": [
        "split", "rsplit", "splitlines", "partition", "rpartition", "join"
    ],
    "Encoding / Formatting": [
        "encode", "format", "format_map", "maketrans"
    ],
    "Magic / Dunder Methods": [
        "__add__", "__class__", "__contains__", "__delattr__", "__dir__", "__doc__",
        "__eq__", "__format__", "__ge__", "__getattribute__", "__getitem__", "__getnewargs__",
        "__getstate__", "__gt__", "__hash__", "__init__", "__init_subclass__", "__iter__",
        "__le__", "__len__", "__lt__", "__mod__", "__mul__", "__ne__", "__new__", "__reduce__",
        "__reduce_ex__", "__repr__", "__rmod__", "__rmul__", "__setattr__", "__sizeof__",
        "__str__", "__subclasshook__"
    ]
}

""" 
1. Case Conversion
| Method       | Syntax             | Explanation                                                                       | Example                                        |
| ------------ | ------------------ | --------------------------------------------------------------------------------- | ---------------------------------------------- |
| `capitalize` | `str.capitalize()` | Capitalizes **first character** of the string and converts the rest to lowercase. | `"hello world".capitalize()` → `"Hello world"` |
| `lower`      | `str.lower()`      | Converts **all characters** to lowercase.                                         | `"HELLO".lower()` → `"hello"`                  |
| `upper`      | `str.upper()`      | Converts **all characters** to uppercase.                                         | `"hello".upper()` → `"HELLO"`                  |
| `title`      | `str.title()`      | Converts the **first character of each word** to uppercase.                       | `"hello world".title()` → `"Hello World"`      |
| `swapcase`   | `str.swapcase()`   | Swaps uppercase to lowercase and **vice versa**.                                  | `"Hello".swapcase()` → `"hELLO"`               |
| `casefold`   | `str.casefold()`   | Similar to `lower()` but **more aggressive** for international characters.        | `"ß".casefold()` → `"ss"`                      |

2. Search & Check
| Method       | Syntax                   | Explanation                                                     | Example                             |
| ------------ | ------------------------ | --------------------------------------------------------------- | ----------------------------------- |
| `find`       | `str.find(substring)`    | Returns **lowest index** of substring, `-1` if not found.       | `"hello".find("l")` → `2`           |
| `rfind`      | `str.rfind(substring)`   | Returns **highest index** of substring, `-1` if not found.      | `"hello".rfind("l")` → `3`          |
| `index`      | `str.index(substring)`   | Like `find()` but **raises error** if substring not found.      | `"hello".index("e")` → `1`          |
| `rindex`     | `str.rindex(substring)`  | Like `rfind()` but **raises error** if substring not found.     | `"hello".rindex("l")` → `3`         |
| `startswith` | `str.startswith(prefix)` | Checks if string starts with given value, returns `True/False`. | `"hello".startswith("he")` → `True` |
| `endswith`   | `str.endswith(suffix)`   | Checks if string ends with given value, returns `True/False`.   | `"hello".endswith("lo")` → `True`   |
| `count`      | `str.count(substring)`   | Returns **number of times** substring occurs.                   | `"hello".count("l")` → `2`          |

"""
