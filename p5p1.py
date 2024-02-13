#1. Write a program that takes as input an integer and prints out a message if the number is negative (Use the if
#construct).

while True:

    user_input_string = input("please give me a number.")

    user_input = int(user_input_string)

    if user_input < 0:
        print(f"{user_input} is negative.")
    else:
        print(user_input)