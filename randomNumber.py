import random

secret_number = random.randint(1, 10)
number = int(input("Guess the number between 1 and 10:"))

if number == secret_number:
    print("well done you guessed the right number!!!")
elif number < secret_number:
    print("To Low")
else:
    print("To High")

print("Secret number:", secret_number)