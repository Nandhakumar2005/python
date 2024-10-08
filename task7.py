'''
AUTHOR:Nandhakumar KS
DATE:8-10-2024
Create,concatenate,and print a string and access a sub-string from a given string
'''

first_name=input('enter your name: ')
last_name=input('enter your name: ')
full_name=(first_name+" "+last_name)
print(full_name)
length=len(full_name)
print(length)
extracted_first_name=full_name[:length-4]
print(extracted_first_name)
