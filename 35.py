'''
    35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

'''

def pri(a,b):
    sum=a+b
    diff=a-b
    if (a==b) or (sum==5) or (diff==5):
        return True
    else:
        return False
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
print(pri(a,b))
