'''
    Write a Python program to parse a string to Float or Integer.
'''

n = "246.2458"
print(float(n))
# print(int(n)) # THIS LINE WILL NOT PRINT BECAUSE IT HAS TO BE CONVERTED IN DOUBLE FORMAT AND N IS IN STRING OF FLOAT 
print(int(float(n)))

n = "246"
print(float(n))
print(int(n)) # THIS LINE WILL PRINT BECAUSE N IS IN STRING OF INT.
print(int(float(n)))
