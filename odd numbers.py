'''
AUTHOR:Nandhakumar KS
DATE:15-10-2024
To write a program to generate n odd numbers
'''

limit=int(input("Enter your limit: "))
odd_number=1
count=0
while count<limit:
    print(odd_number,"\t", end="")
    count+=1
    odd_number+=2
