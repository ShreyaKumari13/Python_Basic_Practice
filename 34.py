'''
    34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

'''
def sum1(a,b):
    if (a+b>=15) and (a+b<=20):
        return 20
    else:
        return a+b
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
print(sum1(a,b))
