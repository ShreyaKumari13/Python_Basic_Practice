'''
    58. Write a Python program to sum of the first n positive integers.

'''
def sum_of(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
n=int(input("Enter the number: "))
print("The sum of number is: ",sum_of(n))