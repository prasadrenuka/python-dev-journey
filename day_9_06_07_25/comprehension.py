# syntax of comprehension
# expression for  in  if condition
# List comprehension
squares = [x**2 for x in [1,2,3]]
print(squares)

# set comprehension
lenWord = {len(x) for x in ['a', 'aaa', 'ab'] if x.__contains__('b')}
print(lenWord)

#dict comprehension
lenWordDic = {word: len(word) for word in ['bananan', 'monkey', 'sim'] }
print(lenWordDic)

# built-in Iteration tools
# zip
names =['renuka', 'prasad', 'yes']
scores = [2,3,4]
print(list(zip(names, scores)))

for index, word in enumerate(names):
    print('indes:',index,'word:',word)

print(sorted([1,4,3]))
print(sorted('baaaabbabnedm'))
print(sorted({1,3,45,6}))
print(sorted({'xyz':'two', 'two':'three'}))

print(list(reversed([1,4,3])))
print(list(reversed('baaaabbabnedm')))
# print(list(reversed({1,3,45,6})))
print(list(reversed({'xyz':'two0', 'two':'three'})))

print(all([True, False, False]))
print(all([True, True, True]))
print(any([True, False, False]))
print(any([True, True, True]))





