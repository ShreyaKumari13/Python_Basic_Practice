'''
    Write a Python program to calculate the sum of three given numbers, if the values 
             are equal then return three times of their sum.
'''
def sumof(a,b,c):
    x=a+b+c
    if a==b==c:
        return(x*3)
    else:
        return(x)
a=int(input("Enter the num1:"))
b=int(input("Enter the num2:"))
c=int(input("Enter the num3:"))
print(sumof(a,b,c))

a=int(input("Enter the num1:"))
b=int(input("Enter the num2:"))
c=int(input("Enter the num3:"))
if a==b==c:
    print((a+b+c)*3)
else:
    print(a+b+c)