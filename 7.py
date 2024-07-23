'''
    Write a Python program to accept a filename from the user and print the extension of that.
'''
file1=input("enter the file name: ")
file_name=file1.split(".")
print(file_name)
print("the extension of the file is:",file_name[-1])