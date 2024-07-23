'''
    Write a Python program which accepts a sequence of
     comma-separated numbers from user and generate a list and a tuple with those numbers
'''
x=input("enter the number separated by comma:")
list=x.split(",")
print(list)
print(tuple(list))


x=int(input("enter the frequency of nmbers to be entered:"))
list=[]
for i in range(x):
    u=int(input("enter the number: "))
    list.append(u)
print(list)
print(tuple(list))


