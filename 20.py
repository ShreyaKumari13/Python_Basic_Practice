'''
    Write a Python program to get a string which is n (non-negative integer) copies of a given string
'''
a=input("Enter the string:")
n=int(input("enter the number of copies:"))
b=a*n
print(b)

def stri(a,n):
    b=a*n
    return b
a=input("Enter the string:")
n=int(input("enter the number of copies:"))
print(stri(a,n))
