import os
import shutil
# copy, copy2, copytree, rmtree, disk_usage, move

#shutil.copy("C:/Users/renuk/PycharmProjects/python-dev-journey/plan.md", "C:/Users/renuk/PycharmProjects/python-dev-journey/MyFolder")
#shutil.copytree("C:/Users/renuk/PycharmProjects/python-dev-journey/MyFolder",
#             "C:/Users/renuk/PycharmProjects/python-dev-journey/new")
#shutil.rmtree('C:/Users/renuk/PycharmProjects/python-dev-journey/new')
# print(shutil.disk_usage("C:/Users/renuk/PycharmProjects/python-dev-journey"))

#Mini Challenge (Try Yourself)

# Create a Python script that:
#
#     Copies a file example.txt to a folder backup/
#
#     Moves the original file to a new folder processed/
#
#     Deletes the folder backup/ after confirming

print(os.getcwd())
#os.mkdir(os.getcwd()+"/Test")
#os.mkdir(os.getcwd()+"/Test/backup")
#os.mkdir(os.getcwd()+"/Test/processed")

#shutil.copy("../MyFolder/random.py",os.getcwd()+"/Test/backup")
#shutil.move("../MyFolder/random.py",os.getcwd()+"/Test/processed")
os.remove("Test/backup/random.py")
#print("diir:",os.chdir('..'))
#print(os.getcwd())