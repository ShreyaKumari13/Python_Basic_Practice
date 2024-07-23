'''
    40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
'''
import math
x1=int(input("Enter the x1 distance: "))
y1=int(input("Enter the y1 distance: "))
x2=int(input("Enter the x2 distance: "))
y2=int(input("Enter the y2 distance: "))
a=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
print("The distance between the points (x1, y1) and (x2, y2) is : ",a)
