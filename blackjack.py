import random
import os
import time

def cls(): #for clearing out console
    os.system('cls' if os.name=='nt' else 'clear')

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


random.seed(time.time())
def hit(list):
    list.append(cards[random.randint(0,12)])

def calc_score(list):
    score = sum(list)
    if score > 21 and 11 in list:
        print("(Ace turned into 1)")
        list[list.index(11)] = 1 ##update the ace value as 1
        return score - 10
    return score


while True: 
    random.seed(time.time()) #change seed in every round
    score = 0
    computer_score = 0 
    computers_cards = [] 
    players_cards = []
    start = input("Start the round? (y/n): ").lower()
    if start == "n":
        break
    elif start != "n" and start != "y":
        input("Wrong input. Try again.")
        cls()
    else:
        cls()
        print(logo)
        hit(computers_cards)
        hit(players_cards)
        hit(players_cards)
        computer_score = calc_score(computers_cards)
        score = calc_score(players_cards)
        print(f"Your hand: {players_cards} => {score}")
        print(f"Computer's hand: {computers_cards} => {computer_score}")
        
        while score < 21:
            hit_again = input("Hit? (y/n): ")
            if hit_again == "y":
                print()
                hit(players_cards)
                score = calc_score(players_cards)
                print(f"Your new hand is {players_cards} => {score}")
                print(f"Computer is {computers_cards} => {computer_score}")
            elif hit_again == "n":
                break
            else:
                input("Wrong input. Try again.")

        while computer_score < 17:
            hit(computers_cards)
            computer_score = calc_score(computers_cards)

        print("\n------------------------")
        print(f"You: {players_cards} => {score}")
        print(f"Computer: {computers_cards} => {computer_score}")
        print("------------------------")

        if score > 21:
            print("You lose.")
        elif computer_score > 21:
            print("You win.")
        elif score == computer_score:
            print("Draw.")
        else:
            if score > computer_score:
                print("You win.")
            else:
                print("You lose.")