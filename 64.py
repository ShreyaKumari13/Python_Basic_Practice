'''
    64. Write a Python program to get file creation and modification date/times. 
'''
import os.path
import time
print("Last modified: %s" % time.ctime(os.path.getmtime("63.py")))
print("Created: %s" % time.ctime(os.path.getctime("63.py")))
