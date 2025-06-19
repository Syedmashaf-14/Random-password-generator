import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total_char=nr_letters+nr_numbers+nr_symbols
user_password = "0"
for number in range(1, nr_letters + 1):
    password = random.choice(letters)
    user_password += password

for number in range(1, nr_symbols + 1):
    pa = random.choice(symbols)
    user_password += pa

for number in range(1, nr_numbers + 1):
    pas = random.choice(numbers)
    user_password += pas

updated_password = user_password.replace("0", "")
print("Password: ", updated_password)

user_choiced_password = list(updated_password)

# now the difficult just simply apply the random function so that passord can be off diff order
diff_pass = "0"
for number in range(1,total_char+1):
    random.shuffle(user_choiced_password)
    diff_pass ="".join(user_choiced_password)

updated_diff_password = diff_pass.replace("0", "")
print("Difficult pass: ", updated_diff_password)
