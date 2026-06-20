a=30
b=40
# if, else, elif
if a<b:
    print("a is greater than b")
elif a==b:
    print('both are equal')
else:
    print('b is greater than a')

# one line if else use it for simple statement ( a if condition else b)
print("a is less than b") if a<=b else print('b is greater than a')

# match case equivalent to switch case
# fruit = input('Enter a fruit name\n')
fruit='ba'
match fruit:
    case 'banana':
        print("it's banana")
    case 'apple':
        print('it\'s apple')
    case 'mango':
        print('it\'s mango')
    case _:
        print('it\'s not fruit')


# assert (not a conditonal statement, It is mainly used for debugging and catching programming mistakes early.)
d=-5
assert d>0, 'a value should be greater than 0'

#Note:
c=()
# "",0,None and empty list[] etch as falsy
if c:
    print('truthsy')
else:
    print('falsy')