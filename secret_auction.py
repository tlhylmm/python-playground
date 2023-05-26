import os
def cls(): #for clearing out console
    os.system('cls' if os.name=='nt' else 'clear')

bidders = {}
max_bid = 0
max_bidder = ""

print("Welcome to the secret auction program.")

other_bidders = "yes"
while other_bidders == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    other_bidders = input("\nAre there any other bidders? Type 'yes' if there are: ")

for key in bidders:
    if bidders[key] > max_bid:
        max_bidder = key
        max_bid = bidders[key]

print(f"The winner is {max_bidder} with a bid of ${max_bid}")