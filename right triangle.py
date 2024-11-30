'''
NAME: Nandhakumar KS
DATE:30-11-2024
A program that accepts the lengths of three sides of a triangle as inputs.The program
should output whether or not the triangle is a right triangle.Implement using functions.
'''

def checking_triangle_is_right_triangle():
    len1 = int(input("Enter the length of first side: "))
    len2 = int(input("Enter the length of second side: "))
    len3 = int(input("Enter the length of third side: "))
    if len1*len1 == len2*len2 + len3*len3 or len2*len2 == len1*len1 + len3*len3 or len3*len3 == len1*len1 + len2*len2:
        print("The given triangle is right triangle.")
    else:
        print("The given triangle is not right angled.")
checking_triangle_is_right_triangle()
checking_triangle_is_right_triangle()
checking_triangle_is_right_triangle()