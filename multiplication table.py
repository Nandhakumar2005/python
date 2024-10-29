'''
AUTHOR:Nandhakumar KS
DATE:29-10-2024
To write a python program to create a multiplication table of a given number.
'''

n=int(input("Enter your number: "))
for i in range(1,13):
    print(n,"*",i,"=",n*i)