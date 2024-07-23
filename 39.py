'''39. Write a Python program to compute the future value of a specified principal amount, compounded annually.
    Test Data : amt = 10000, int = 3.5, years = 7
    Expected Output : 12722.79
    
'''
amt = 10000
inte = 3.5
years = 7
future = amt*((1+(0.01*inte)) ** years)
print(future)