# os

import os
print(len(dir(os)))
print(os.getcwd())
print(os.listdir())
os.chdir("C:/Users/renuk/PycharmProjects/python-dev-journey/day_11_11_07_25")
print(os.getcwd())
print(os.listdir())
#print(os.mkdir('Test'))
#print(os.makedirs('parent/test'))
#os.rmdir('Test')
#os.rmdir('parent') # rmdir only removes the empty folders
# os.remove("parent/test/test.html")
print(os.path.exists("collectionsModule2.py"))
print(os.path.abspath("collectionsModule2.py"))
# print(os.path.isfile("myfile.txt"))     # Is it a file?
# print(os.path.isdir("myfolder"))        # Is it a folder?

# getcwd, chdir, listdir, mkdir, makedirs rmdir, remove, os.path.exists, isfile, isdir, abspath

## Practice Task:

# Write a script that:
#     Creates a folder called MyFolder
#     Changes to that folder
#     Prints the current path
#     Lists all files (should be empty)
#     Goes back to the original directory
print("Practise task")
originalDir = os.getcwd()
os.chdir("C:/Users/renuk/PycharmProjects/python-dev-journey")
os.mkdir("MyFolder")
os.chdir(os.getcwd()+"/MyFolder")
print(os.getcwd())
print(os.listdir())
os.chdir(originalDir)
print(os.getcwd())
