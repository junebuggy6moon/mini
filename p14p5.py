def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

user_num = int(input("Give me a number of terms from the Fibonacci Series."))

# check if the number of terms is positive
if user_num <= 0:
    print("it has to be a positive number, please try again!")

for n in range(user_num):
    print(fibonacci(n))

