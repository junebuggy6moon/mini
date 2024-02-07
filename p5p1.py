#1. Write a program that takes as input an integer and prints out a message if the number is negative (Use the if
#construct).

while True:

    user_input = int(input("please give me a number."))

    if user_input < 0:
        print("It's negative.")
    else:
        print(user_input)