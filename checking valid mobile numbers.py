'''
NAME: Nandhakumar KS
DATE:30-11-2024
Program to check whether the given number is a valid mobile number or not using functions.
'''


def mobile_numbers():
    mobile_number = input("enter mobile number:")
    if len(mobile_number)==10 and mobile_number[1] in "7,8,9":
        print("Given number is valid.")
    else:
        print("Given number is not valid.")
mobile_numbers()
mobile_numbers()