'''
    57. Write a Python program to get execution time for a Python method.
    sum of numbers from 1 to 5
'''
import time
def sumofnumbers(n):
    start=time.time()
    s=0
    for i in range(1,n+1):
        s=s+i
    end=time.time()
    return s,end-start
n=int(input("enter the number: "))
print("The sum of number and taken for the execution of the program is: ",sumofnumbers(n))