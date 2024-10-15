'''
AUTHOR:Nandhakumar KS
DATE:15-10-2024
To determine the smallest of three numbers.
'''

num1=int(input("Enter your number 1: "))
num2=int(input("Enter your number 2: "))
num3=int(input("Enter your number 3: "))
if num1<num2 and num1<num3:
    print("Number 1 is the smallest")
elif num2<num1 and num2<num3:
    print("Number 2 is the smallest")
else:
    print("Number 3 is the smallest")