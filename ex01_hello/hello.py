"""Calculates your BMI based on input and gives feedback."""
print("Welcome to Body mass index (BMI) calculator.")

# 1. part- the irrelevant stuff.
person_name = input("What is your name?")
while person_name == "":
    print("Name was not inserted!")
    person_name = input("What is your name?")
else:
    person_school = input("What school do you go to?")
while person_school == "":
    print("School was not inserted!")
    person_school = input("What school do you go to?")
else:
    print(person_name + ", welcome to " + person_school)

# 2. part- the actual calculator.
person_weight = input("Weight in kg:")
while person_weight == "":
    print("Weight was not inserted!")
    person_weight = input("Weight in kg:")
else:
    person_height = input("Height in meters:")
while person_height == "":
    print("Height was not inserted!")
    person_height = input("Height in meters:")

BMI1 = float(person_weight) / float(person_height) ** 2
if BMI1 < 18.5:
    conclusion = "alakaaluline"
elif 24.9 > BMI1 >= 18.5:
    conclusion = "normaalkaal"
else:
    conclusion = "ülekaaluline"

ymardamine_a = 1
BMI2 = round(BMI1, ymardamine_a)
# ümardamine n kohani pärast punkti.

print(str(BMI2) + ", " + conclusion)
