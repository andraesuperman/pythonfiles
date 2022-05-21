import random

random_number = random.randint(1, 10)
guess = int(input("Guess the lucky number: "))

if (random_number == guess):
    print("You guessed the lucky number!")

else:
    print("uh oh! You guess is wrong") 

