'''
     Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
        Sample value of n is 5
        Expected Result : 615
'''
n = input("Enter a number : ")
a,b,c,sum1 = n,n*2,n*3,0
a,b,c = int(a),int(b),int(c)
sum1 = a+b+c
print("  "+str(a))
print(" "+str(b))
print(c)
print("____")
print(sum1)
print("____")