'''
    Write a Python program to create a histogram from a given list of integers
    
'''
def printpa(list,x):
    for i in list:
        print(i*x)
list=[4,3,5,6]
x=input("enter: ")
printpa(list,x)


a="@"
list=[]
a=int(input("enter the frequency of number you want to enter: "))
for i in range(a):
    b=int(input("Enter the number:"))
    list.append(b)
print(list)
for i in list:
    print(i*"@")


list=[1,2,3,4,5]
for i in list:
    print(i*"@")