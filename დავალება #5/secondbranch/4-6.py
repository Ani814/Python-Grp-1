import random


#4

text = input("შეიყვანე ტექსტი: ")

cleaned = ""

for char in text.lower():
    if char.isalnum():
        cleaned += char

if cleaned == cleaned[::-1]:
    print("ეს არის პალინდრომი")
else:
    print("ეს არ არის პალინდრომი")

    # ერთი სიმბოლოს წაშლით შემოწმება
    found = False

    for i in range(len(cleaned)):
        temp = cleaned[:i] + cleaned[i+1:]

        if temp == temp[::-1]:
            print("ახლო პალინდრომი:", temp)
            found = True
            break

    if not found:
        print("ახლო პალინდრომი ვერ მოიძებნა")


#5
        

word = input("შეიყვანე ერთი სიტყვა: ")

if " " in word:
    print("მხოლოდ ერთი სიტყვა შეიყვანე!")
else:
    nicknames = [
        word + "Master",
        "Dark" + word,
        word + "X",
        word + "Pro",
        "The" + word
    ]

    random.shuffle(nicknames)

    print("ზედმეტსახელები:")
    for nick in nicknames:
        print(nick)


#6


numbers = input("შეიყვანე რიცხვები გამოტოვებით: ").split()

numbers = [int(num) for num in numbers]

print("""
1 - ზრდადობით
2 - კლებადობით
3 - random
4 - მხოლოდ უნიკალური
""")

choice = input("აირჩიე: ")

if choice == "1":
    print(sorted(numbers))

elif choice == "2":
    print(sorted(numbers, reverse=True))

elif choice == "3":
    random.shuffle(numbers)
    print(numbers)

elif choice == "4":
    print(list(set(numbers)))

else:
    print("არასწორი არჩევანი")
