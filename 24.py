'''
    Write a Python program to test whether a passed letter is a vowel or not
    
'''
x=input("Enter the letter: ")
if x in ('a','e','i','o','u'):
    print("its a vowel")
else:
    print("consonants")

def vowel(x):
    if x in ('a','e','i','o','u'):
        print("its a vowel")
    else:
        print("consonants")
x=input("Enter the letter: ")
vowel(x)


def vowel(x):
    char="aeiou"
    return x in char
x=input("Enter the letter: ")
print(vowel(x))