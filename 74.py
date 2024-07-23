'''
    74. Write a Python program to hash a word.

'''
int_val="w3r"
str_val = 'GeeksforGeeks'
flt_val = 24.56
print ("The string hash value is : ",str(hash(int_val)))
print ("The string hash value is : ",str(hash(str_val)))
print ("The float hash value is : ", str(hash(flt_val)))

soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
word=input("Input the word be hashed: ")
word=word.upper()
coded=word[0]
for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])
print() 
print("The coded word is: "+coded)
print()
