import random
import string


#1

while True:
    length = input("შეიყვანე პაროლის სიგრძე: ")

    if not length.isdigit():
        print("მხოლოდ რიცხვი შეიყვანე!")
        continue

    length = int(length)
    break

use_upper = input("გინდა დიდი ასოები? (yes/no): ").lower()
use_lower = input("გინდა პატარა ასოები? (yes/no): ").lower()
use_digits = input("გინდა რიცხვები? (yes/no): ").lower()
use_symbols = input("გინდა სიმბოლოები? (yes/no): ").lower()

characters = ""

if use_upper == "yes":
    characters += string.ascii_uppercase

if use_lower == "yes":
    characters += string.ascii_lowercase

if use_digits == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation

if characters == "":
    print("აირჩიე მინიმუმ ერთი ვარიანტი!")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("გენერირებული პაროლი:", password)


#2


password = input("შეიყვანე პაროლი: ")

score = 0

if len(password) >= 8:
    score += 2

if any(char.isdigit() for char in password):
    score += 2

if any(char in string.punctuation for char in password):
    score += 2

if any(char.isupper() for char in password):
    score += 2

if any(char.islower() for char in password):
    score += 2

if len(set(password)) < len(password) / 2:
    score -= 2

if score < 4:
    strength = "weak"
elif score < 8:
    strength = "medium"
else:
    strength = "strong"

print("ქულა:", score, "/10")
print("პაროლი არის:", strength)


#3

def fibonacci(n):
    numbers = [0, 1]

    while len(numbers) < n:
        numbers.append(numbers[-1] + numbers[-2])

    return numbers[:n]


while True:
    user_input = input("შეიყვანე რიცხვი: ")

    if user_input.isdigit():
        user_input = int(user_input)
        break

    elif user_input.isalpha():
        print("შენ შემოიტანე ასო, მხოლოდ რიცხვი!")

    else:
        print("შენ შემოიტანე სიმბოლო, მხოლოდ რიცხვი!")

print(fibonacci(user_input))
