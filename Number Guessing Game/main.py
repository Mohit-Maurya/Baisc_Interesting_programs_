from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!\n\nI am thinking of a number between 1 and 100.")
find_num = random.randint(1, 100)
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy" or difficulty == "hard":
        break
    else:
        print("Kindly write the right word.")
if difficulty == "easy":
    attempts = 10
else:
    attempts = 6

def game(attempts, find_num):
    print(f"You have {attempts} attempts remaining to guess the number.")
    while True:
        guess = int(input("Make a guess: "))
        if guess in range(1, 101):
            break
        else:
            print("Please make a guess in between 1 and 100.")
    
    attempts -= 1
    
    if guess > find_num:
        print("Too high.")
    elif guess < find_num:
        print("Too low.")
    else:
        print(f"You got it! The number was {find_num}.")
        return 0
    if attempts <= 0:
        print(f"You lost! The number was {find_num}.")
        return 0
    game(attempts, find_num)

game(attempts, find_num)
