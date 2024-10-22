'''
AUTHOR:Nandhakumar KS
DATE:22-10-2024
To write a python program to convert temperature values back and forth between Celsius
and Fahrenheit.The user should be able to input a temperature in Celsius and Fahrenheit,
and the program should convert it to the other unit using the formula.
'''


temperature=input("Is this in Celsius or Fahrenheit: ")
temperature_value=int(input("Enter your temperature value: "))
if temperature=="c":
    f=(9/5*temperature_value)+32
    print(temperature_value,"Celsius is",f,"Fahrenheit")
elif temperature=="f":
    c=5/9*(temperature_value-32)
    print(temperature_value,"Fahrenheit is",c,"Celsius")
