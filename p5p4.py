#Write a program that takes as input an integer and prints out one of the following messages indicating whether
#the number is in one of the specified ranges:
# Number is equal to 0
# Number is greater than 0 and less than or equal to 20
# Number is greater than 20 and less than or equal to 40
# Number is greater than 40 and less than or equal to 60
# Number is greater than 60 and less than or equal to 80
# Number is greater than 80 and less than or equal to 100
# Number is greater than 100
# If the number entered is less than 0, a message should be printed out to that effect.

zero_bound=0
first_bound=20
second_bound=40
third_bound=60
fourth_bound=80
fifth_bound=100

number_between_string_message="Number is greater than {} and less than or equal to {}"

user_input_strng = input("Please give me a number: ")

number=int(user_input_strng)

if number < zero_bound:
    print(f"The number entered is less than {zero_bound}")
elif number == zero_bound:
    print(f"Number is equal to {zero_bound}")
elif number <= first_bound:
    print(number_between_string_message.format(zero_bound,first_bound))
elif number <= second_bound:
    print(number_between_string_message.format(first_bound,second_bound))
elif number <= third_bound:
    print(number_between_string_message.format(second_bound,third_bound))
elif number <= fourth_bound:
    print(number_between_string_message.format(third_bound,fourth_bound))
elif number <= fifth_bound:
    print(number_between_string_message.format(fourth_bound,fifth_bound))
elif number > fifth_bound:
    number(f"Number is greater than {fifth_bound}")
