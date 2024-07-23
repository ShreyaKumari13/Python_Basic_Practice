'''
    91. Write a Python program to swap two variables.

'''

x = [5,10]
temp = x[0]
x[0] = x[1]
x[1] = temp
print('The value of x after swapping: ',x)

a = 30
b = 20
print("\nBefore swap a = %d and b = %d" %(a, b))
a, b = b, a
print("\nAfter swaping a = %d and b = %d" %(a, b))
print()


