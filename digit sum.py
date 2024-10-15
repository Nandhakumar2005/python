'''
AUTHOR:Nandhakumar KS
DATE:15-10-2024
A program to find the sum of digits of a given number.
'''

num=int(input("Enter your number: "))
sum=0
while num>0:
    r=num%10
    num=num//10
    sum=sum+r
print("sum of digits of the number: ",sum)