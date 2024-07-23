'''
    49. Write a Python program to list all files in a directory in Python.
'''
from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/VS Code/shreya 123') if isfile(join('/VS Code/shreya 123', f))]
print(files_list)
