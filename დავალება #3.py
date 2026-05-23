#1

products = {
    'rocket' : 15000,
    'spaceship' : 25000,
    'helmet' : 5000
    }

print(f"""
Hello, you are visiting SpaceX.

Products:
rocket - $15000
spaceship - $25000
helmet - $5000
""")

wishlist = []
total = 0


item = input('Which items would you like to buy? Press "0" if you are done.')

while item != "0":
    if item in products:
        wishlist.append(item)
        total += products[item]
        print(f'{item} added to cart.')
    else:
        print('This product does not exist.')
    item = input('Which items would you like to buy? Press "0" if you are done.')


print(f"\nYour items: {wishlist}")
print(f"Total price: ${total}")


confirm = input("Do you want to buy these items? (yes/no): ")

if confirm == "yes":
    print("Purchase successful!")
else:
    print("Purchase cancelled.")



#2

for i in range(1, 21):
    if i % 2 == 0:
        print(f'{i} - ლუწია')
    else:
        print(f'{i} - კენტია')

j = 1

while j < 21:
    if j % 2 == 0:
        print(f'{j} - ლუწია')
    else:
        print(f'{j} - კენტია')
    j += 1


#3

students = {
    'Ana' : [89,66,12,75,11],
    'Giorgi' : [67,72,90,91,55],
    'Levant' : [49,36,88,98,34],
    'Veronika' : [99,88,32,65,99],
    'Nika' : [77,81,41,73,99]
    }

print(students)

for student in students:
    average_grade = sum(students[student]) / len(students[student])

    print(f"{student}'s average grade is {average_grade:.2f}")


#4

current_year = 2026

age = input('Enter your age, please, enter "q" if you want to stop: ')

while age != 'q':

    try:
        age = int(age)

        birth_year = current_year - age

        print(f'You were born in {birth_year}.')

    except ValueError:
        print("That's not an age.")

    age = input('Enter your age, please, enter "q" if you want to stop: ')


#5

mylist = range(100)

i = 0

squares = []
cubes = []

while i < len(mylist):
    squares.append(mylist[i] ** 2)
    cubes.append(mylist[i] ** 3)
    i += 1

print("Squares:", squares)
print("Cubes:", cubes)


#6

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()


#7
''' the issue was that numbers on the list are strings,
you can/'t sum them without turning them into integers or another numeric type.'''

numbers = ["1", "2", "3", "4"]
total = 0

for n in numbers:
    total += int(n)


print("Total:", total)


#8

data = ["5", 0, "3", True, "", 2, "x", False]
total = 0

for item in data:

    if isinstance(item, str) and item.isdigit():
        total += int(item)

    elif isinstance(item, int) and not isinstance(item, bool):
        total += item

    elif isinstance(item, bool) and item is True:
        total += 1

print("Total:", total)

    
#9

transactions = {
    "გიო": "100",
    "ნიკა": 50,
    "აკაკი": "30a",
    "ლევანი": 0,
    "ანა": "70",
    "მარი": True
}

total = 0

for value in transactions.values():

    if isinstance(value, str) and value.isdigit():
        total += int(value)

    elif isinstance(value, int) and not isinstance(value, bool):
        total += value

    elif isinstance(value, bool) and value is True:
        total += 1

print("Total:", total)


#10

secret_number = 27
attempts = 0

while True:

    guess = input("Guess the number (0-51) or type 'exit': ")

    if guess == "exit":
        print("Game over.")
        break

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess < 0 or guess > 51:
        print("რიცხვი სცდება არეალს")
        continue

    attempts += 1

    if guess == secret_number:
        print(f"გილოცავ გამოიცანი {secret_number} რიცხვი, მცდელობა: {attempts}")
        break
    else:
        print("არასწორია, სცადე კიდევ ერთხელ.")



