import random
import time
import os

def cls(): #for clearing out console
    os.system('cls' if os.name=='nt' else 'clear')
    



while True:
    random.seed(time.time())
    number = random.randint(0,100)
    cls()
    print("Welcome to number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while True:
        if difficulty == "easy" or difficulty == "hard":
            break
        else:
            input(f"Wrong input. The input is {difficulty} Try again.")
            cls()
            print("Welcome to number guessing game!")
            difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    lives = 10
    if difficulty == "hard":
        lives = 5

    for i in range(lives):
        print(f"You have {lives - i} attempts left.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You won with {i + 1} guesses!")
            play_again = input("Type 'yes' if you wanna play again: ")
            if play_again == "yes":
                break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

        if i + 1 == lives:
            print("You ran out of lives!. You lost.") 
            play_again = input("Type 'yes' if you wanna play again: ")
            break

    if play_again != "yes":
        cls()
        break