'''
AUTHOR:Nandhakumar KS
DATE:15-10-2024
To check whether the given number is positive or not.
'''

number=int(input("Enter a number: "))
if number>0:
    print("The given number is: ",number,"is positive.")
elif number<0:
    print("The given number is: ",number,"is negative.")
else:
    print("the given number:",number,"is zero")