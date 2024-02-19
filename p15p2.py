 
def f(n):
    if n == 1:
        print("f(n) = 1")
        return 1

    elif n > 1:
        answer = f(n - 1) + 2 ** (n - 1)
        print(f"f({n}) = f({n} - 1) + 2 ** ({n} - 1) = {(answer - 1)} + {2 ** (n - 1)} = {answer}")
        return answer

user_input = input("Please enter an number: ")
int_input = int(user_input)

if int_input < 1:
    print("The number you entered must be equal or greater than 1.")

print(f(int_input))
