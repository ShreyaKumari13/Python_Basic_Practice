'''
  Write a Python program to concatenate all elements in a list into a string and return it.
'''

def concatenate(list):
    result=""
    for element in list:
        result=result+str(element)
    return result
print(concatenate([1, 5, 12, 2]))


''' 
   note:  join is used only for string
   
'''
list=['1','2','32','45']
print(list)
print("".join(list))