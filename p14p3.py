# Implement the program that searches for prime numbers in a range of integers and demonstrates the use of
# the else clause in a for loop in Python from recent lectures (Lecture 13) (Page 16 of the notes). Ensure that
# you understand how this program works.

user_num = input("Please enter a number: ")
int_num = int(user_num)

if int_num % 2 == 0:
    print("It's not a prime number")
else:
    print("It's prime number")
