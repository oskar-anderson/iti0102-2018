"""Would you like to join itük dialogue."""
print("Welcome to itük!")
person_name = input("what is your name?")
print("Hi there, " + person_name + "!")
decision = input("Would you like to join itük?")
if decision == "Yes!":
    print("Welcome to the club!")
elif decision == "No.":
    print("Why tho?")
else:
    print("Ok, see you next year!")
