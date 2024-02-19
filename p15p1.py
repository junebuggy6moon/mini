def f(n):
    if n == 1:
        print("f(1) = 2")
        return 2
    elif n > 1:
        answer = n + f(n - 1)
        print(f"f({n}) = {n} + f({n-1}) = {n} + {answer - n} = {answer}")
        return answer

user_input = input("Please enter a number: ")
int_input = int(user_input)

if int_input < 1:
    print("The number you entered must be greater than 0.")

print(f(int_input))

