'''
AUTHOR:Nandhakumar KS
DATE:15-10-2024
To write a program to generate n odd numbers
'''

limit=int(input("Enter your limit: "))
odd_number=1
while odd_number<limit:
    print(odd_number,"\t", end="")
    odd_number+=2
