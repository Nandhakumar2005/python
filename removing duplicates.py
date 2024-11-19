'''
NAME:Nandhakumar KS
DATE:19-11-2024
To remove duplicates from a list using a loop or set.
'''

list = [12,10,12,10,20,20,30,30,25,10]
unique_list = []
for number in list:
    if number not in unique_list:
        unique_list.append(number)
print("The original numbers in list is:",list)
print(unique_list)
print(list.count(10))