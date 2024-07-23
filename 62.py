'''
    62. Write a Python program to convert all units of time into seconds. 

'''
def secon(d,e,f):
    days_to_seconds=days*24*60*60
    hours_to_seconds=hours*60*60
    minutes_to_seconds=minut*60
    seconds=days_to_seconds+hours_to_seconds+minutes_to_seconds
    return seconds
days=int(input("Enter the days: "))
hours=int(input("Enter the hours: "))
minut=int(input("Enter the minutes: "))
print("The total seconds are: ",secon(days,hours,minut))
