'''
NAME:Nandhakumar KS
DATE:19-11-2024
Input two lists from the user.Merge these lists into a third list such that in the
merged list, all even numbers occur first followed by odd numbers.Both the even
numbers and odd numbers should be in sorted order.
'''\

list1 = []
list2 = []
list1_size = int(input("Enter the size of list1: "))
print("Enter the element of list1: ")
for i in range(list1_size):
    list1.append(int(input()))
#entering list 2
list2_size = int(input("Enter the size of list2: "))
print("Enter the element of list2: ")
for i in range(list2_size):
    list2.append(int(input()))
print(list1,list2)
#combining list
combined_list = list1+list2
print(combined_list)
even_list = []
odd_list = []
for i in combined_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
even_list.sort()
odd_list.sort()