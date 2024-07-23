'''
    61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.

'''
d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %d inches." % d_inches)
print("The distance in yards is %f yards." % d_yards)
print("The distance in miles is %f miles." % d_miles)
