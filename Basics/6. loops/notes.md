| Loop Type    | Syntax                   | Example                                 | Output                                   |
|--------------|--------------------------|-----------------------------------------|------------------------------------------|
| `for`        | `for item in iterable:`  | `for i in [1,2,3]: print(i)`            | `1 2 3`                                  |
| `while`      | `while condition:`       | `while x < 4:`                          | Runs until condition becomes False       |
| Nested Loop  | Loop inside another loop | `for i in range(3): for j in range(2):` | Multiple iterations                      |
| `break`      | Exit loop immediately    | `if i == 3: break`                      | Loop stops                               |
| `continue`   | Skip current iteration   | `if i == 3: continue`                   | Skip iteration                           |
| `pass`       | Placeholder, do nothing  | `if i == 3: pass`                       | No effect                                |
| `for-else`   | Else runs if no break    | `for ... else:`                         | Executes else if loop completes normally |
| `while-else` | Else runs if no break    | `while ... else:`                       | Executes else if loop completes normally |


for variable in iterable:

| Type        | Iterable? | Example            |
|-------------|-----------|--------------------|
| List        | ✅ Yes     | `[1, 2, 3]`        |
| Tuple       | ✅ Yes     | `(1, 2, 3)`        |
| String      | ✅ Yes     | `"python"`         |
| Dictionary  | ✅ Yes     | `{"a":1, "b":2}`   |
| Set         | ✅ Yes     | `{1, 2, 3}`        |
| Range       | ✅ Yes     | `range(5)`         |
| File Object | ✅ Yes     | `open("file.txt")` |
| Integer     | ❌ No      | `10`               |
| Float       | ❌ No      | `10.5`             |
| Boolean     | ❌ No      | `True`             |

Dictionary

By default, loops over keys:

person = {
    "name": "Renuka",
    "age": 28
}

for key in person:
    print(key)

Output:

name
age

Values:

for value in person.values():
    print(value)

Both:

for key, value in person.items():
    print(key, value)