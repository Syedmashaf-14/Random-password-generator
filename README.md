## 🔐 PyPassword Generator
This Python script is a customizable password generator that lets users specify how many letters, symbols, and numbers they want in their password. It then generates a password with those constraints and shuffles it to increase difficulty and randomness.

## ✅ Features:
User inputs number of letters, symbols, and digits.

Random characters are selected from predefined character pools.

The password is then shuffled to ensure a strong and unpredictable format.

Outputs both the ordered password and the shuffled (difficult) password.

## 📌 How it works:
Takes input from the user:

Number of letters

Number of symbols

Number of numbers

Combines randomly chosen characters into a string.

Converts the string into a list and applies random.shuffle() to randomize the character positions.

## Displays both:

Simple password (in the order generated)
![image](https://github.com/user-attachments/assets/7175a799-8623-4426-8e81-078f00e09f22)


Shuffled password (more secure)

🧪 Example:
pgsql
Copy
Edit
Welcome to the PyPassword Generator!
How many letters would you like in your password?
> 4
How many symbols would you like?
> 2
How many numbers would you like?
> 3
Password:  aBcD&*123
Difficult pass:  B2&a13c*D
💡 Notes:
Initial "0" used as a dummy character is removed before printing.

Shuffling is done after forming the complete password to increase strength.

Ensure input is a positive integer.
