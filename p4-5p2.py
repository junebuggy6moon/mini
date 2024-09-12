# Write a program that takes as input a single length (a float) and calculates the following:
# • The area of a square with side of that length
# • The volume of a cube with side of that length
# • The area of a circle with radius of that length
# • The volume of a sphere with radius of that length
# • The volume of a cylinder with radius of that length and side of that length
# Import the math module and use the constant math.pi for the value π.
# When the length is entered by the user, the program should check that it is non-negative. If the length is
# negative, the message “Length must be >= 0. Please try again.” should be printed out and the program
# should exit.

import math

user_input_string = float(input("Please gives me a length: \n"))

user_input_length = float(user_input_string)

square = user_input_length * user_input_length
volume = user_input_length ** 3
circle = math.pi * (user_input_length ** 2)
sphere_v = (4/3) * math.pi * (user_input_length ** 3)
cylinder_v = math.pi * (user_input_length ** 2) * user_input_length

if user_input_length < 0:
    print("Length must be >= 0. Please try again.")
else:
    print(square)
    print(volume)
    print(circle)
    print(sphere_v)
    print(cylinder_v)







