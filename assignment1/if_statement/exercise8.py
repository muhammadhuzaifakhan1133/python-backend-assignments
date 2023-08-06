# Write a program to ask user its name and check whether name consists of 5 or more letters

name = input("Enter name: ")
if len(name) >= 5:
    print("Valid")
else:
    print("Invalid")