"""
Python Notes: Functions, Methods, Attributes, Objects, print vs return, Semicolons

Read this file top-to-bottom and run sections one by one.
Everything is explained using comments.
"""

# ============================================================
# 1. FUNCTION
# ============================================================

# A function is a reusable block of code.

def greet(name):
    return f"Hello {name}"


print("Function Example:")
print(greet("Renuka"))  # Calls the function and prints the returned value


# ============================================================
# 2. METHOD
# ============================================================

# A method is a function that belongs to an object.

name = "python"

# upper() belongs to the string object "python"
print("\nMethod Example:")
print(name.upper())  # PYTHON

# Function vs Method
print(len(name))     # len() is a function
print(name.upper())  # upper() is a method


# ============================================================
# 3. ATTRIBUTE
# ============================================================

# Attributes are data stored inside an object.

class Person:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    def greet(self):      # method
        print(f"Hello, I am {self.name}")


p = Person("Renuka", 28)

print("\nAttributes Example:")
print(p.name)
print(p.age)

print("\nMethod Example Inside Class:")
p.greet()

# Rule:
# p.name     -> attribute (data)
# p.greet()  -> method (behavior)


# ============================================================
# 4. EVERYTHING IN PYTHON IS AN OBJECT
# ============================================================

# Every value is an object created from a class.

print("\nTypes:")
print(type(10))         # int object
print(type("hello"))    # str object
print(type([1, 2, 3]))  # list object
print(type(True))       # bool object

# Objects have methods and attributes.

x = 10

print("\nMethods Available on int object:")
print("bit_length" in dir(x))

print(x.bit_length())


# ============================================================
# 5. FUNCTIONS ARE OBJECTS TOO
# ============================================================

def hello():
    return "Hi"

print("\nFunctions Are Objects:")
print(type(hello))

# Function assigned to another variable
another_ref = hello

print(another_ref())


# ============================================================
# 6. FUNCTION OBJECT VS FUNCTION CALL
# ============================================================

def greet_again():
    return "Hello"

print("\nFunction Object vs Function Call:")

# Function object
print(greet_again)

# Function execution
print(greet_again())

# Remember:
# greet_again    -> function object
# greet_again()  -> execute function


# ============================================================
# 7. METHOD OBJECT VS METHOD CALL
# ============================================================

text = "python"

print("\nMethod Object vs Method Call:")

# Method object
print(text.upper)

# Method execution
print(text.upper())

# Remember:
# text.upper    -> method object
# text.upper()  -> execute method


# ============================================================
# 8. print() VS return
# ============================================================

def add_using_print(a, b):
    print(a + b)

print("\nprint() Example:")
result = add_using_print(2, 3)

# add_using_print prints 5
# but returns nothing
# Python automatically returns None

print(result)


def add_using_return(a, b):
    return a + b

print("\nreturn Example:")
result = add_using_return(2, 3)

print(result)

# Difference:
#
# print()  -> display output on screen
# return   -> send value back to caller


# ============================================================
# 9. SEMICOLON (;)
# ============================================================

# Python does not require semicolons.

a = 10; b = 20

print("\nSemicolon Example:")
print(a + b)

# Trailing semicolon is valid
c = 100;

print(c)

# Semicolons are rarely used in Python because
# Python prefers one statement per line.


# ============================================================
# SUMMARY
# ============================================================

"""
Function:
    greet()

Method:
    "hello".upper()

Attribute:
    p.name

Object:
    10, "hello", [1,2,3], functions, classes

print():
    Displays output

return:
    Sends value back to caller

greet:
    Function object

greet():
    Function execution
"""
