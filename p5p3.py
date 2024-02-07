#3. Write a program that takes as input a floating-point number and prints out whether the number is positive,
#negative or equal to 0.

while True:
    user_input = float(input("Please give me a number: "))

    if user_input > 0:
        print("It's positive.")
    elif user_input < 0:
        print("It's negative.")
    else:
        print("It's Zero.")