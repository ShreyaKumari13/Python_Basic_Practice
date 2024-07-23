'''
    84. Write a Python program to count the number occurrence of a specific character in a string.

'''
a='Karn the surya putra was the warrior remembered from ages.'
print(a.count("a"))
print(a.count("u"))
print(a.count("m"))

a='Karn the surya putra was the warrior remembered from ages'
count=0
for i in a:
    if (i=='a'):
        count=count+1
    else:
        # print("not found")
        pass
print(count)