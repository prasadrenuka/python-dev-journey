from collections import Counter
# It is Dictionary SubClass which Counts how many times each items appears

data =['banana', 'apple', 'orange', 'apple', 'banana', 'apple']
dataTuple = tuple(data)
print(dataTuple)
# c = Counter(data)
c = Counter(data) # retrun data key, value pair dict
print(c)
print(c['banana'])
print(c['apple'])
print(c['orange'])
print(c.most_common(1)) # return list in tuple [(,),(,)]

# string
text = "hello World"
tc = Counter(text)
print(tc)
print(tc['l'])

a = Counter('hello')
b = Counter('world')
print('a',a)
print('b',b)
print(a + b)
print( 'subtracting Counter',a+b)

sentence = "banana apple orange apple banana banana"
# Step 1: Split the string into words
words = sentence.split()
print('splitted Words', words)
# Step 2: Use Counter to count each fruit
max = Counter(words)
print(max)
# Step 3: Print most common fruit
print(max.most_common(1))