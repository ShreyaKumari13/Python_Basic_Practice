'''
    43. Write a Python program to get OS name, platform and release information.
'''
import platform
import os
print("Name of the operating system:",os.name)
print("Name of the OS system:",platform.system())
print("Version of the operating system:",platform.release())