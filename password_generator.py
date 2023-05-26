#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

'''
password = ""
for i in range(0,nr_letters):
  password += random.choice(letters)
for i in range(0,nr_symbols):
  password += random.choice(symbols)
for i in range(0,nr_numbers):
  password += random.choice(numbers)
print(password)
'''
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

'''
length = int(nr_letters) + int(nr_numbers) + int(nr_symbols)
password = ""
letters_counter = 0
symbols_counter = 0
numbers_counter = 0
while len(password) < length:
  x = random.randint(0,2) #0-numbers 1-symbols 2-numbers
  if x == 0 and letters_counter != nr_letters: 
    password += random.choice(letters)
    letters_counter += 1
  elif x == 1 and symbols_counter != nr_symbols: 
    password += random.choice(symbols)
    symbols_counter += 1   
  elif x == 2 and numbers_counter != nr_numbers:
    password += random.choice(numbers)
    numbers_counter += 1

print(password)
'''

#There is an easy method:
#Just do it like in the first method
#Then shuffle the string by adding this to end:

password = random.sample(password,len(password)) #turn string to list by using sample()
random.shuffle(password) #shuffle the list
password = "".join(password) #join the list and make it a string again