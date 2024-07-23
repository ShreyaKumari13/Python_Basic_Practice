""" Write a Python program to get the n (non-negative integer) copies of the first 
    2 characters of a given string. Return the n copies of
    the whole string if the length is less than 2.
"""
a="abcdefgh"
n=2
print(n*(a[0:2]))


def stri(a,n):
    c=a[0:2]
    d=n*c
    return d
a=input("Enter the string:")
n=int(input("enter the number of copies:"))
print(stri(a,n))
