'''
AUTHOR:Nandhakumar KS
DATE:29-10-2024
TO write a python program to find if a number is prime.
'''

n=int(input("Enter your number: "))
isprime = True
for i in range(2,(n//2)+1):
    if n % i ==0:
        isprime = False
        break
if isprime:
    print("The given number",n,"is prime.")
else:
    print("The given number",n,"is not prime.")