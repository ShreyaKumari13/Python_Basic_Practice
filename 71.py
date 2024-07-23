'''
    71. Write a Python program to get a directory listing, sorted by creation date.

'''
import glob
import os

files = glob.glob("*.py")
files.sort(key=os.path.getctime)
print("\n".join(files))