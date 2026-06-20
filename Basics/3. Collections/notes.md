| Feature             | List `[]`           | Tuple `()`   | Dictionary `{key:value}` | Set `{}`                |
|---------------------|---------------------|--------------|--------------------------|-------------------------|
| Ordered?            | ✅ Yes               | ✅ Yes        | ✅ Yes (Python 3.7+)      | ❌ No                    |
| Mutable?            | ✅ Yes               | ❌ No         | ✅ Yes                    | ✅ Yes                   |
| Duplicates Allowed? | ✅ Yes               | ✅ Yes        | ❌ Keys No (Values Yes)   | ❌ No                    |
| Indexing Supported? | ✅ Yes               | ✅ Yes        | ❌ By key only            | ❌ No                    |
| Key-Value Pair?     | ❌ No                | ❌ No         | ✅ Yes                    | ❌ No                    |
| Add Item            | `append()`          | Not possible | `dict[key]=value`        | `add()`                 |
| Remove Item         | `remove()`, `pop()` | Not possible | `pop(key)`               | `remove()`, `discard()` |
| Loop Supported?     | ✅ Yes               | ✅ Yes        | ✅ Yes                    | ✅ Yes                   |
| Common Use          | Collection of items | Fixed data   | Lookup table             | Unique values           |
