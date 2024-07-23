'''
     Write a Python program to get the difference between a given number and 17, 
       if the number is greater than 17 return double the absolute difference
'''
num1=int(input("Enter the first num1:"))
num2=17
a=num1-17
if num1>17:
    print("the number is:",a+a)
else:
    print(a)
