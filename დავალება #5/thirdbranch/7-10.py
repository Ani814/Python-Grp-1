#7

text = input("შეიყვანე ტექსტი: ")

result = ""

for char in text:
    if char.isalpha() or char.isspace():
        result += char

print(result)


#8

numbers = input("შეიყვანე რიცხვები მძიმით: ").split(",")

numbers = [int(num) for num in numbers]

while len(numbers) > 1:
    print(numbers)

    new_row = []

    for i in range(len(numbers) - 1):
        new_row.append(numbers[i] + numbers[i + 1])

    numbers = new_row

print(numbers)


#9

text = input("შეიყვანე ტექსტი: ").lower()

words = text.split()

counter = {}

for word in words:
    counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())

most_common = []

for word, count in counter.items():
    if count == max_count:
        most_common.append(word)

print("ყველაზე ხშირი სიტყვა/სიტყვები:", most_common)


#10

sentence = input("შეიყვანე წინადადება: ")

words = sentence.split()

result = {}

for word in words:
    result[word] = len(word)

print(result)
