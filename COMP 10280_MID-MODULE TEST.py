# I am not sure where to put the while loop and some elements are missing but I couldn't figure it out.

user_number = input("Enter a non-negative integer: ")
int_input = int(user_number)

def divisor(number):
    if number < 0:
        print("The number you entered must be positive.")
        return

    by_3 = 0
    by_5 = 0
    by_7 = 0
    by_11 = 0

    if current_number % 3 == 0:
        by_3 += 1
    if current_number % 5 == 0:
        by_5 += 1
    if current_number % 7 == 0:
        by_7 += 1
    if current_number % 11 == 0:
        by_11 += 1

    print(f"Number of numbers divisible by 3: {by_3}")
    print(f"Number of numbers divisible by 5: {by_5}")
    print(f"Number of numbers divisible by 7: {by_7}")
    print(f"Number of numbers divisible by 11: {by_11}")

divisor(int_input)