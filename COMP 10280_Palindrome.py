user_word = input("Please enter a word: ")
def reverse(user_word):
    x = ""
    for i in range(len(user_word)):
        x += user_word[len(user_word)-1-i]

    return x

print(reverse(user_word))

reversed_word = reverse(user_word)

if reversed_word == user_word:
    print("it's a palindrome")
else:
    print("It's NOT a palindrome.")

