'''
    Write a Python program to find whether a given number (accept from the user) 
         is even or odd,print out an appropriate message to the user
'''

def oddeven(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
n=int(input("Enter the num: "))
oddeven(n)

