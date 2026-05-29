# ===================== Task 1 =====================
print("\n#1 ხმოვანი თუ თანხმოვანი")

letter = input("შემოიტანე ასო: ").strip().lower()

vowels = "აეიოუ"

if len(letter) != 1:
    print("გთხოვთ შეიყვანოთ მხოლოდ ერთი ასო")
elif letter in vowels:
    print(f'"{letter}" ხმოვანია')
else:
    print(f'"{letter}" თანხმოვანია')


# ===================== Task 2 =====================
print("\n#2 რიცხვები 10-დან 0-მდე")

for i in range(10, -1, -1):
    print(i, end=" ")

print()


# ===================== Task 3 =====================
print("\n#3 ლისტში 3 უდიდესი რიცხვი და მათი ინდექსები")

import random

lst = [random.randint(1, 20) for _ in range(10)]
print(lst)

sorted_with_index = sorted(
    enumerate(lst),
    key=lambda x: x[1],
    reverse=True
)

top3 = sorted_with_index[:3]

for i, (idx, val) in enumerate(top3, 1):
    print(f"მონაცემი {i}: {val} (ინდექსი {idx})")


# ===================== Task 4 =====================
print("\n#4 ოთხკუთხედის დაბეჭდვა")

width = int(input("შეიყვანე სიგანე: "))
height = int(input("შეიყვანე სიმაღლე: "))

for _ in range(height):
    print("# " * width)


# ===================== Task 5 =====================
print("\n#5 არითმეტიკული ოპერაციები")

def arithmetic_operations(x, y):
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")
    print(f"{x} * {y} = {x * y}")

    if y != 0:
        print(f"{x} / {y} = {x / y}")
        print(f"{x} // {y} = {x // y}")
        print(f"{x} % {y} = {x % y}")
    else:
        print("0-ზე გაყოფა არ შეიძლება")

x = int(input("შეიყვანე x: "))
y = int(input("შეიყვანე y: "))

arithmetic_operations(x, y)


# ===================== Task 6 =====================
print("\n#6 ოთხკუთხედის ფუნქციად გადაკეთება")

def print_rectangle(width, height):
    for _ in range(height):
        print("# " * width)

print_rectangle(5, 2)

print()

print_rectangle(2, 5)


# ===================== Task 7 =====================
print("\n#7 სიმბოლოს რაოდენობა სტრიქონში")

def count_char(string, char):
    count = string.count(char)
    print(f'სიმბოლო "{char}" გვხვდება {count}-ჯერ')

count_char("John and Jane Doe", "J")


# ===================== Task 8 =====================
print("\n#8 სიტყვების რაოდენობის დათვლა")

def wc(sentence):
    words = sentence.split()
    print(f"სიტყვების რაოდენობა: {len(words)}")

wc("რამდენიმე სიტყვა რომლის დათვლასაც ვაპირებთ")


# ===================== Task 9 =====================
print("\n#9 Hangman")

def hangman():
    words = ["python", "computer", "game", "algorithm", "hangman"]

    secret_word = random.choice(words)

    guessed_letters = set()

    attempts = 10

    print("სიტყვის გამოცნობა ('exit' გასასვლელად)")

    while attempts > 0:

        display = ""

        for char in secret_word:
            if char in guessed_letters:
                display += char + " "
            else:
                display += "_ "

        print(display)

        # თუ ყველა ასო გამოცნობილია
        if all(char in guessed_letters for char in secret_word):
            print("გილოცავ!")
            return

        guess = input("შეიყვანე ასო ან სიტყვა: ").lower().strip()

        if guess == "exit":
            print("თამაში დასრულდა")
            return

        # სრული სიტყვის გამოცნობა
        if guess == secret_word:
            print("გილოცავ!")
            return

        # ერთი ასოს შეყვანა
        if len(guess) == 1:
            if guess in secret_word:
                guessed_letters.add(guess)
                print("სწორია")
            else:
                attempts -= 1
                print("არასწორია")
        else:
            attempts -= 1
            print("არასწორი სიტყვა")

        print(f"დარჩენილი ცდები: {attempts}")

    print(f"თქვენ დამარცხდით! სიტყვა იყო: {secret_word}")

hangman()


# ===================== Task 10 =====================
print("\n#10 მარჯვენა / მარცხენა თამაში")

def left_right_game():

    for i in range(5):

        correct_answer = random.choice(["მარჯვენა", "მარცხენა"])

        user_choice = input(
            f"ცდა {i+1}/5 - აირჩიე (მარჯვენა/მარცხენა) ან 'exit': "
        ).strip().lower()

        if user_choice == "exit":
            print("თამაში დასრულდა")
            return

        if user_choice != correct_answer:
            print(f"შენ დამარცხდი! სწორი პასუხი იყო: {correct_answer}")
            return

        print("სწორია!")

    print("გამარჯვება!")

left_right_game()
