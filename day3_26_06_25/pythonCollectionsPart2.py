# list [] ordered, mutable, duplicates are allowed, .append and .remove, only same type we can add or remove
# tuple () ordered, non-mutable, duplicates are allowed, n/a, n/a
# dictionary{"key":value} unordered, key-value pair, mutable,  should have unique key, modify using key, any type of value can be assigned to key
# set {} unordered, mutable, duplicates are not allowed, .add and .remove, only same type we can add or remove
duplicates = (10, 10, 50)
print(duplicates[2])
print(duplicates)
set_now = {1, 6, 3, 3} # duplicat entries are not allowed {1, 2, 3}
print(set_now)
print(set_now)
print(set_now)

# how to access set since it's unordered indexing is not supported
## check value present in set
print(6 in set_now)
print(0 in set_now)
## loop
for value in set_now:
    print(value)
set_now.add(90)
# set_now.add("testing_multiple") we can't add other types
print(set_now)

my_list =[2,3,4]
print(my_list)
# my_list.append('renuka') we can't add other types in list too
## convert to list
converted_set=list(set_now)
print(converted_set)
print(converted_set[3])

print((1,1,1,1))