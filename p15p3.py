#There is a bug that I don't know how to fix. when print, it loops the base case result mutiple times.

def f(n):
    if n == 0:
        print("f(0) = 13")
        return 13

    elif n == 1:
        print("f(1) = 8")
        return 8

    elif n > 1:
        answer = f(n - 2) + 13 * f(n - 1)
        print(f"f({n}) = f({n} - 2) + 13 x f({n} - 1) = {answer}")
        return answer

user_input = input("Please enter a number: ")
int_input = int(user_input)

if int_input < 0:
    print("The number you entered must be positive.")

print(f(int_input))
