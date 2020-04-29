import random
import string
'abcdefghijklmnopqrstuvwxyz'
x = random.choice(string.ascii_letters).lower()
userLetter = ""
print(x)
while userLetter != x:
    userLetter = input("Enter a letter:\n").lower()

    if userLetter == x:
        print("Correct!")

    else:
        userLetter = input("Wrong, try again:\n")