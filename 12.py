''' 
    Write a Python program to print the calendar of a given month and year
    
'''
import calendar   
yy = int(input("enter the year in four digit: "))
mm = int(input("enter the month in two digit: "))
print(calendar.month(yy, mm)) 

print (calendar.calendar(yy))