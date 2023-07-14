# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
random_letters = []
random_symbols = []
random_numbers = []
password_letters = ''
password_symbols = ''
password_numbers = ''

for _ in range(nr_letters):
    random_letters.append(random.choice(letters))
    password_letters = ''.join(random_letters)
for _ in range(nr_symbols):
    random_symbols.append(random.choice(symbols))
    password_symbols = ''.join(random_symbols)
for _ in range(nr_numbers):
    random_numbers.append(random.choice(numbers))
    password_numbers = ''.join(random_numbers)

eazy_password = password_letters + password_symbols + password_numbers
print(eazy_password)

# Hard level
eazy_password_list = list(eazy_password)
random.shuffle(eazy_password_list)
hard_password = ''.join(eazy_password_list)
print(hard_password)
