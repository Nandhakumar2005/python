'''
AUTHOR:Nandhakumar KS
DATE:29-10-2024
To write a python program to see how many consonants and vowels
there are in a word.
'''

string_input=input("Enter a string: ")
vowels ="aeiouAEIOU"
consonants ="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vowels_count=0
consonants_count=0
for char in string_input:
    if char in vowels:
        vowels_count=vowels_count+1
    else:
        consonants_count=consonants_count+1
print("The number of vowels in", string_input, "is", vowels_count)
print("The number of consonants in",string_input,"is",consonants_count)