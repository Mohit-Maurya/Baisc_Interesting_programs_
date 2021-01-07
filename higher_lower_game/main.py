from art import logo, vs
from game_data import data
from replit import clear
import random

#Choose 2 random data
A = random.choice(data)
B = random.choice(data)

#compare A and B 'follower_count' 
def compare_AB(a, b):
    if a > b:
        return "a"
    else:
        return "b"

#Print logo AND compare A - vs - Against B
def compare_print(compare):
    compare_string = f"{compare['name']}, a {compare['description']}, from {compare['country']}."
    return compare_string

def gui(A, B):
    print(logo)
    print("Compare A: " + compare_print(A))
    print(vs)
    print("Against B: " + compare_print(B))

# main game function
def game(A, B):
    score = 0
    while True:
        gui(A, B)
        #print(A['follower_count'], B['follower_count'])
        #take input A or B
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear()
        #if right then increase score by 1 else terminate the game by writing final score.
        #print(guess)
        if guess == compare_AB(A['follower_count'], B['follower_count']):
            score += 1
            A, B = B, random.choice(data)
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
            
game(A, B)
