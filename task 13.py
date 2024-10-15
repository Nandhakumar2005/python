'''
AUTHOR:Nandhakumar KS
DATE:15-10-2024
To determine the entry ticket fare in a zoo based on age.
'''

age=int(input("Enter your age: "))
if age<10:
    print("Please pay 7")
elif age>=10 and age<60:
    print("Please pay 10")
else:
    print("Please pay 5")
    