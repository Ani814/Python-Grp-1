# 1

var1 = 1
var2 = -1
var3 = True

print(var1, var2, var3)

# save variable types into the variables
var1 = type(var1)
var2 = type(var2)
var3 = type(var3)
print(var1, var2, var3, end = '\n')


#2

var4 =False
var5 =3
var6 = {"key":"value", "key1":"value", "key3":"value"}

print(var4, var5, var6)

# change the types of the variables using type casting

var4 = float(var4)
var5 = float(var5)
var6 = list(var6.items())  # without the .items() method, only keys are saved in the list
print(var4, var5, var6)


#3

dict_group = {
    'name' :'Python2023', 'count' : 35,
    'male' : 22, 'female' : 13, 
    'Student1' : 24, 'Student2' : 33,
    'Student3' : 15, 'Student4' : 45,
    'Student5' : 42
    }


#4


birth_year = 1997
name = 'ანი'
surname = 'ბრეგვაძე'
current_year = 2026

age = current_year - birth_year

print(f"მე {name} {surname} დავიბადე {birth_year} წელს, შესაბამისად ვარ {age} წლის.")



#5

yes = 119
no = 82
total = yes + no
yes_percent = (yes / total) * 100
no_percent = (no / total) * 100

print(f"YES: {yes} = {yes_percent:.2f}%")
print(f"NO: {no} = {no_percent:.2f}%")



#6


seconds = 3670

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print(f"{hours} საათი {minutes} წუთი {remaining_seconds} წამი")


# 7

text = "Python"

print("პირველი ასო:", text[0])
print("ბოლო ასო:", text[-1])


# 8

math = 45
total = 60

percent = (math / total) * 100

print(f"პროცენტი: {percent:.2f}%")


# 9

birth_year = 2000
current_year = 2025

age_next_year = (current_year - birth_year) + 1

print(f"მომავალ წელს შენ იქნები {age_next_year} წლის")


# 10

minutes = 350

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{hours} საათი და {remaining_minutes} წუთი")
