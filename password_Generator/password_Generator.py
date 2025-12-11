import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to the Password Generator!")

n_letters = int(input("How many letters you want in your password?\n"))
n_numbers = int(input("How many numbers you want in your password?\n"))
n_symbols = int(input("How many symbols you want in your password?\n"))

# Build password
password_list = []

# Add letters
for _ in range(n_letters):
    password_list.append(random.choice(letters))

# Add numbers  
for _ in range(n_numbers):
    password_list.append(random.choice(numbers))

# Add symbols
for _ in range(n_symbols):
    password_list.append(random.choice(symbols))

# Shuffle and create final password
random.shuffle(password_list)
password = ''.join(password_list)  # More efficient than loop

print(f"Your password: {password}")
print(f"Password length: {len(password)} characters")