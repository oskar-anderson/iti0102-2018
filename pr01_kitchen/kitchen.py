"""Kitchen Dialogue"""
print("Welcome to the kitchen.")
name = input("What is your name?")
print("Hi there, " + name + "!")
drink = input("What would you like to drink?")
if drink == "tea":
    print("Have a nice tea!")
elif drink == "coffee":
    print("Feeling tired?")
else:
    print("We only serve water.")
