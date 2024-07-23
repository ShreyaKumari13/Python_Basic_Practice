'''
    Write a Python program that will accept the base and height of a triangle and compute the area
'''
def areatri(base,height):
    area=(1/2)*base*height
    return area

base=int(input("Enter the base: "))
height=int(input("Enter the height: "))
print(areatri(base,height))