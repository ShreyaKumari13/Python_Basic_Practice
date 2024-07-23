'''
    Write a Python program to calculate number of days between two dates.
'''
from datetime import date
f_date = date(2021, 4, 27)
l_date = date(2021, 5, 31)
delta = l_date - f_date
print(delta.days)


