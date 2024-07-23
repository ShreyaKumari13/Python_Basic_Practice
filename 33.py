'''
    33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

'''


def sum1(a,b,c):
    if (a==b) or (b==c) or (c==a):
        return 0
    else:
        return a+b+c
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
print(sum1(a,b,c))






a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
sum=0
if (a==b) or (b==c) or (c==a):
    print('The sum of the num is',sum)
else:
    print("The sum of the number is",a+b+c)
