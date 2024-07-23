'''
    32. Write a Python program to get the least common multiple (LCM) of two positive integers. 

'''

import math
a = int(input("Enter the first number : "))
b = int(input("Enter the Second number : "))
print(math.lcm(a,b))

x = int(input("Enter the first number : "))
y = int(input("Enter the Second number : "))
if x>y:
    smaller=x
else:
    smaller=y
for i in range(1,smaller+1):
    if x%i==0 & y%i==0:
        hcf=i
lcm = (x*y)/hcf
print("The lcm of the given number is: ",lcm)