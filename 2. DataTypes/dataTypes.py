# String (str)
name = 'Renuka Prasad S'
name2 = "Renuka"

'''end of the line is not necessary and not preferred but if you 
want to declare multiple variable in single line it comes in handy'''
print(name);
print(name2)
print(type(name))

#multiline
name3 = """renuka
prasad s"""
print(name3)

# int
age = 27
print(age)
print(type(age))
print(f'int method and attributes {len(dir(int))}')
print(dir(int))

# boolean
is_coding = True
print(type(is_coding))
print(is_coding)
print(f'boolean method and attributes {len(dir(bool))}')
print(dir(bool))

# complex
com = 2 + 3j
print(com)
print(type(com))
print(f'complex method and attributes {len(dir(complex))}')
print(dir(complex))

# float
salary = 27000.67
print (salary)
print(type(salary))
print(f'float method and attributes {len(dir(float))}')
print(dir(float))

'''
1. bool is subclass of int hence methods and attributes of both are same
'''