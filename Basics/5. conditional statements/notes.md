1. if
2. if-else
3. if-elif-else
4. and / or / not
5. Ternary
6. match-case
7. assert

| Statement      | Syntax                            | Example                                               | Result                                            |
|----------------|-----------------------------------|-------------------------------------------------------|---------------------------------------------------|
| `if`           | `if condition:`                   | `if age >= 18:`                                       | Executes block if condition is True               |
| `if-else`      | `if condition: ... else:`         | `if age >= 18: print("Adult") else: print("Minor")`   | Chooses one of two paths                          |
| `if-elif-else` | `if ... elif ... else:`           | `if marks >= 90: ... elif marks >= 75: ... else: ...` | Checks multiple conditions                        |
| Nested `if`    | `if c1: if c2:`                   | `if age >= 18: if license:`                           | Inner block runs only if both conditions are True |
| `and`          | `condition1 and condition2`       | `if age > 18 and salary > 30000:`                     | True only when both conditions are True           |
| `or`           | `condition1 or condition2`        | `if age >= 18 or permission:`                         | True if at least one condition is True            |
| `not`          | `not condition`                   | `if not is_raining:`                                  | Reverses True/False                               |
| Ternary        | `value1 if condition else value2` | `"Adult" if age >= 18 else "Minor"`                   | One-line if-else                                  |
| `match-case`   | `match var: case value:`          | `match day: case 1:`                                  | Matches a value against cases                     |
| `assert`       | `assert condition, "message"`     | `assert age > 0, "Invalid age"`                       | Raises `AssertionError` if condition is False     |
