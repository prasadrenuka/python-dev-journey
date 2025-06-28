# problem statement
# Write a function called describe_person that takes:
#
# Any number of hobbies (*args)
#
# Any person details like name, age (**kwargs)
#
# describe_person("reading", "coding", name="Renuka", age=27)
# Try this on your own or let me know if you'd like the answer!
from functools import reduce


def describe_person(*hobbies, **persondetails): # *args **kwargs here args and kwargs are just name not key word , *&** are important here
    # for hobby in args:
        print('hobbies', hobbies)
        print('personDetails', persondetails)

describe_person("reading", "coding", name="Renuka", age=27)

# *
def add(*numbers):
    total =0
    for number in numbers:
        total+=number
    return  total

print(add(1,3,4,5,6,8.9))

# **
def print_info(**details):
    for key, value in details.items():
        print(key,'=',value)

print_info(name='renuka', age=27, profession='coding', location='bangalore') # don't use '' for keyword

# lambda
# can't be reused again one time use
add = lambda a,b: a+b # syntax lambda(keyword) arguments separated by comma: expression
print(add(9,2))

#Write a lambda that:
# Takes 2 strings
# Returns True if they are the same length

checkIfEqual = lambda str1, str2: len(str1) == len(str2)

print(checkIfEqual("apple", "grape")) # true


# map() apply function to each element
a= [1,2, 3,4] #list

print(list(map(lambda x: x**2, a)))
def powerr(x):
    return x**2

print('xxxx', list(map(powerr, a)))

# filter() filter if it satisfies the condition

print(list(filter(lambda x: x%2==0, a)))

# reduce() always expects the function to take exactly 2 arguments — no more, no less.
print(reduce(lambda c,b: c*b, a))
# flow
# addition
# 1+2 =3
# 3+3 =6
# 6+4 =10