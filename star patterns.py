'''
NAME:Nandhakumar KS
DATE:19-11-2024
Program to construct patterns of stars(*),using a nested for loop.
'''

#increasing triangle pattern
limit = int(input("Enter the limit: "))
for i in range(limit+1):
    for j in range (i):
        print("*",end=" ")
    print()
print()#Decreasing star pattern
for i in range(limit,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
print()#Hill pattern
for i in range(1,limit+1):
    for j in range (limit-i):
        print(" ",end=' ')
    for k in range (2*i-1):
        print("*",end=" ")
    print()
print()#Reverse hill pattern
for i in range(limit,0,-1):
    for j in range (limit-i):
        print(" ",end=' ')
    for k in range (2*i-1):
        print("*",end=' ')
    print()