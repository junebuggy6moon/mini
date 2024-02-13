#2. Write a program that takes as input an integer and prints out whether the number is non-negative or not (Use
# the if ... else construct)

while True:

    user_input_string = input("Please give me a number.")

    user_input = int(user_input_string)

    if user_input >= 0:
        print(f"The number {user_input} is non negative.")
    else:
        print(f"The number {user_input} is negative.")



