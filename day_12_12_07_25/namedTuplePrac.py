import math
from collections import namedtuple
from math import floor

# syntax:

# different way of declaring namedtuple
#point = namedtuple('point', ['x', 'y'])
#point = namedtuple('point','x y')
point = namedtuple('point',('x','y') )

# instance of point
p= point(20,30)
# can't do like this below
#p.x = 10
# workaround create new instace with different value
new_p = p._replace(x=1)
print(new_p)

# adding multiple entries
# p = [
#     point(23,30),
#     point(2,3)
# ]
# access using instances
print(p)
print(p.x)
print(p.y)
# accessing multiple entries
# print(p[0].x, p[0].y, p[1].x, p[1].y)

# get an error adding the new attribute
# p.z =3


## Mini Challenge
# Problem Statement:
#
# You're given a list of students with their name, age, and department.
# Use a namedtuple to store each student record and:
#
#     Create a list of all students.
#
#     Print the names of all students from the "CSE" department.
#
#     Find the average age of all students.

# input: [
#     ("Alice", 21, "CSE"),
#     ("Bob", 22, "ECE"),
#     ("Charlie", 20, "CSE"),
#     ("David", 23, "ME"),
#     ("Eva", 21, "CSE")
# ]

students = namedtuple('students',['name', 'age','branch'])

instances = [
    students("Alice", 21, "CSE"),
    students("Bob", 22, "ECE"),
    students("Charlie", 20, "CSE"),
    students("David", 23, "ME"),
    students("Eva", 21, "CSE")
 ]

# allAge =0
# for instance in instances:
#     if instance.branch == 'CSE':
#         print(instance.name)
#     allAge+=instance.age

# imporved versions

cse_students =[ instance.name for instance in instances if instance.branch == 'CSE']
average_age = sum( i.age for i in instances)/len(instances)

print('average age of all students',average_age)
print('cse_students', cse_students)




