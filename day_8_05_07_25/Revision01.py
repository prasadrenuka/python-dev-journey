# Data Types: defines the data that is being stored

## int, str, float, boolean, complex
## syntax example:
### num= 10,
### name = 'python', (or) name = "python"
### num = 10.20
### isIt = True,  (or) False
### comp = 1+2j

### no need to predefine the variable
### multiline for string """
# go"""
### print() out put statement

# Collections : stores the collection of data

## List, tuple, Dictionary, Set
## syntax example:
### myList = [1,2,3,4,5,5] ordered, allows duplicate, mutable, accessed using index(ex: myList[0])
### myList.append(6) add 6 to the last of mylist, myList.remove(4) removes the specified value

### myTuple = (1,3,3,4) ordered, allows duplicate, immutable, accessed using index(ex: myTuple(1))

### myDictionary = {"name":'renuka', 'age':26, 'salary':45000.00} unordered, unique key is needed, mutable,
### accessed using key (myDictionary['name']) , myDictionary['age']=27 , myDictionary['company'] = 'accenture'

### mySet = {1,3,4} unordered, doesn't allow duplicates, mutable, accessed using loop since it's unordered,
### mySet.add(5), mySet.remove(3)

# ConditionStatements: statements which checks condition perfoms action based on it
## if else, if elif else, match, assert
## syntax example:
### if a > b:
##      print(a)
### match 'name':
###       case 'renuka':
###         print('renuka')
###       case _:
###         print('default')
### assert a>0, 'a value should be greater than zero,

# Note: revisit 'match' syntax, default case syntax 'assert'

# operators
## Arthematic: +,-,*,/,//, %, **
## comparioson: >,<,>=,<=,==,!=
## logical: and, or, not
## Assignment: =, +=,-=,*=,/=, **=, //=, %=
## Identity operators: is, is not (compares if both object pointing to same)
## membership operators: in, not in (works on collections and string) check if values is collections except dictionary checks only for keys

# Note: revisit Identity operatiors, membership operators,

# functions: code resuable perfoms particular set of action
## def function_name():
###       return

# loops: performs repetative set of action, break, continue, pass
## for in :
##    print()
## while :
##    print()

# Note: revisit break, continue, pass

# Note: revisit functions>advancedTopics, *,**, map, filter, reduce
# Note: revisit everything from day05