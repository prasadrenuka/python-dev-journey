from numpy import sort
#List
print('---------------List---------------')
fruit =["apple", "banana", "mango"]
print(fruit)

'''how to add and remove list?
.append appends at the last of list'''
fruit.append("grapes")
print(fruit)
print(f'number of methods and attribute in lists is {len(dir(list))} and they are {dir(list)}')
#.remove removes the specified value
fruit.remove("banana")
print(fruit)

# how to modify?
fruit[1] ="waterMelon"
print(fruit)

# access
print(fruit[1])

# how to loop
for frui in fruit:
    print(frui)

# fruit.remove("random") # throws an ValueError: list.remove(x): x not in list
# allows duplicates
fruit.append('grapes')
print(fruit)

# Tuple
print('---------------Tuple---------------')
coordinates = (10, 20)
print(coordinates)

# ordered
print(coordinates)

'''mutable?
# tuple don't support mutability
# coordinates[0]= 20
'''

# access
print(coordinates[0])

# more than one iteam?
coordinates2 =(10, 30, 50)
print(coordinates2)

print(f'number of methods and attribute in tuple is {len(dir(tuple))} and they are {dir(tuple)}')
# dictionary
print('---------------Dictionary---------------')
#syntax
personalDetails = {"name":"Renuka Prasad S", "age": 27, "profession":"software engineer"}
print(personalDetails)

# unordered?
print(personalDetails)

# access
print(personalDetails["name"])
print(personalDetails["age"])

# modify
personalDetails["age"] = 28
print(personalDetails)

# add
personalDetails["location"] ="bangalore"
print(personalDetails)

# loop
for key, value in personalDetails.items():
    print(key,"=", value)

print(f'number of methods and attribute in dictionary is {len(dir(dict))} and they are {dir(dict)}')
# unordered vs ordered??
# unordered means order of entry is not maintained
# order mean order of entry is maintained
print('-------------Set-----------------')
# set
num={1234, 1235, 1236}
print(num)
print(num)

# add or remove
num.add(86)
print(num)

num.remove(1236)
print(num)

print(1235 in num)
print(f'number of methods and attribute in dictionary is {len(dir(set))} and they are {dir(set)}')
a =(('b',3), ('a',6))
print(sort(a))