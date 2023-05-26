import random
import time
import os
random.seed(time.time())

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def cls(): #for clearing out console
    os.system('cls' if os.name=='nt' else 'clear')

word_list = ["aardvark", "baboon", "camel"]
lives = 6
chosen_word = random.choice(word_list)
length = len(chosen_word) 

current_word = []
for letters in chosen_word:
    current_word += "_"

gameover = False
while not gameover:    
    cls()
    print('''  ___      _                    ___                                
 / _ \    | |                  / _ \                               
/ /_\ \ __| | __ _ _ __ ___   / /_\ \___ _ __ ___   __ _  ___ __ _ 
|  _  |/ _` |/ _` | '_ ` _ \  |  _  / __| '_ ` _ \ / _` |/ __/ _` |
| | | | (_| | (_| | | | | | | | | | \__ \ | | | | | (_| | (_| (_| |
\_| |_/\__,_|\__,_|_| |_| |_| \_| |_/___/_| |_| |_|\__,_|\___\__,_|
                                                                   
                                                                   ''')
                                                                   
    print(current_word)
    print(stages[lives])
    print(f"Current lives: {lives}")
    guess = input("Guess a letter: ").lower()
    match = False
    if len(guess) != 1:
        input("Incorrect entry. Try again.")
        match = True
    if guess in current_word:
        input("Given letter is already opened. Try again.")
    for i in range(length):
        if guess == chosen_word[i]:
            current_word[i] = guess
            match = True
    if match == False:
        lives -= 1
    if "_" not in current_word:
        gameover = True
        print(f"{chosen_word.upper()}!!! You win.")
    if lives == 0:
        gameover = True
        print(f"Game over. The word was {chosen_word}.")