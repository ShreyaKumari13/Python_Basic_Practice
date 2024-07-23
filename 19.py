"""
    Write a Python program to get a new string from a given string where "Is" has been added to the front. 
     If the given string already begins with "Is" then return the string unchanged
"""
a=input("Enter the sentence:")
b=a.split(" ")
print(b)
if b[0] != "Is":
    b.insert(0,"Is")
    print(b)
    print(" ".join(b))
else:
    print(b)
    print(" ".join(b))





