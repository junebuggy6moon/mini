#3. Write a program that takes as input a floating-point number and prints out whether the number is positive,
#negative or equal to 0.

while True:
    user_input_string = float(input("Please give me a number: "))

    user_input = float(user_input_string)

    if user_input > 0:
        print(f"{user_input} is positive.")
    elif user_input < 0:
        print(f"{user_input} is negative.")
    else:
        print("It's Zero.")