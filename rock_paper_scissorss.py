import random

'''
THERE IS A SHORTER WAY!!

if 0-1-2 dışında bir sayı girilmişse:
    print error
else
    kazanan üç durum için üç adet iki condition içeren if statement
    else
        you lose
'''


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice = int(input("Please choose: 0-Rock / 1-Paper / 2-Scissors\n"))

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice ==  2:
    print(scissors)
    
print("Computer choose:")

computer = random.randint(0,2)

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer ==  2:
    print(scissors)

if choice == computer:
    print("Draw")

elif choice == 0: #user picked rock
    if computer == 1:
        print("You lose")
    elif computer == 2:
        print("You win")
        
elif choice == 1: #user picked paper
    if computer == 0:
        print("You win")
    elif computer == 2:
        print("You lose")
        
elif choice == 2: #user picked scissors
    if computer == 0:
        print("You lose")
    elif computer == 1:
        print("You win")
        
        