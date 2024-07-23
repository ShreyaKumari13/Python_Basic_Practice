'''
    36. Write a Python program to add two objects if both objects are an integer type.

'''

def sahi(a,b):
    if isinstance(10,int) and isinstance(11.1,int):
        print("True hai")
    else:
        print("false hai")
a=10
b=11.1
sahi(a,b)



def sahi(a,b):
    if not(isinstance(a,int) and isinstance(b,int)):
        raise TypeError("Num should be integer")
    return a+b
print(sahi(10,11.1))