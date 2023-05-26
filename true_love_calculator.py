print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#  T R U E ------  L O V E

name1 = name1.lower()
name2 = name2.lower()

t = name1.count("t")
t += name2.count("t")
r = name1.count("r")
r += name2.count("r")
u = name1.count("u")
u += name2.count("u")
e = name1.count("e")
e += name2.count("e")

firstdigit = t + r + u + e

l = name1.count("l")
l += name2.count("l")
o = name1.count("o")
o += name2.count("o")
v = name1.count("v")
v += name2.count("v")

secondigit = l + o + v + e

score = str(firstdigit) + str(secondigit)
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")