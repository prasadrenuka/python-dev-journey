# using an absolute path
# file = open("C:\\Users\\renuk\PycharmProjects\python-dev-journey\README.md", 'r')
# relative path
#file = open('log.txt', 'r')
# relative folder structure
# file = open('../README.md', 'r')
# file = open('../day6_29_06_25/log.txt', 'r') # read
# file = open('../day6_29_06_25/log.txt', 'a') # append
# print(type(file))
# file.write('\nLearning Python file handling') # write
# content = file.read()
#print(type(content))
# print(content)
# file.close()
# import os
# print(os.getcwd())
# print()

# using 'with' (.close() is not necessary)
with open('log.txt','r') as file:
    print(file.read())

# without close() what will happen? (waste of resource and other consequences)
file = open('log.txt','r')
print(file.read())
file.close()

# each line
with open('log.txt', 'r') as file:
    for line in file:
        print('line:', line.strip())

