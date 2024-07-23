'''
    42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
'''
import sys
print(sys.version)
print(sys.version_info)

import struct
print(struct.calcsize("P") * 8)