print("Welcome to Py Password Generator")
import random
# easy level password
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4',
           '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&',
           '(', ')', '*', '+']

nr_letters=int(input("Number of letters you want ?? "))
nr_symbols=int(input("Number of symbols you want?? "))
nr_numbers=int(input("Number of integer you want?? "))

password=""

for char in range(0,nr_letters):
    password+=random.choice(letters)

for char in range(0,nr_symbols):
    password+=random.choice(symbols)
for char in range(0,nr_numbers):
    password+=random.choice(numbers)

print(f"Your password is:- {password}")


# hard level password


import random

print("Welcome to PyPassword Generator!")

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4',
           '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&',
           '(', ')', '*', '+']

# User input
nr_letters = int(input("How many letters? "))
nr_symbols = int(input("How many symbols? "))
nr_numbers = int(input("How many numbers? "))

# Empty password list
password_list = []

# Generate letters
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

# Generate symbols
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# Generate numbers
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list
random.shuffle(password_list)

# Convert list into string
password = ""

for char in password_list:
    password += char

# Display final password
print(f"Your password is: {password}")
