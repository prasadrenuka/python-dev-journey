# defaultdict: just like normal dict assignes default value
# syntax: defaultdict(type)
## type: list,set,str,int
### * tuple can also be used but immutable so there is no real use

# Problem Statement:
#
# You are given a list of words. Group* the words by their first letter and store them in a dictionary.
from collections import defaultdict
words = ["apple", "ant", "banana", "bat", "cat", "camel"]
output = defaultdict(list)

for word in words:
    output[word[0]].append(word)

print("The words are gouped by their first letter",output)


