'''
AUTHOR:Nandhakumar KS
DATE:22-10-2024
TO find prime numbers upto a given n number.
'''

n=int(input("Enter your number: "))
for n in range(2,n+1):
    isprime = True
    for i in range(2,(n//2)+1):
        if n % i == 0:
            isprime=False
    if isprime:
        print(n,end=" ")