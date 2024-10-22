'''
AUTHOR:Nandhakumar KS
DATE:22-10-2024
To write a python program to find the largest of three numbers.The program should take
three numbers as input from the user and determine which one is the largest.Use
conditional statements to compare the numbers.
'''

num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
num3=int(input("Enter your third number: "))
if num1>num2 and num1>num3:
    print("First number is the largest.")
elif num2>num1 and num2>num3:
    print("Second number is the largest.")
else:
    print("Third number is the largest.")