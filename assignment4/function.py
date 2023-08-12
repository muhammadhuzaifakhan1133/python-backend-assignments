# Write a program to create a function that takes two arguments, name and age. print them inside function.

def person(name, age):
    print(f"{name} is {age} years old.")

person("Huzaifa", 20)

# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name, salary=9000):
    print(f"The salary of {name} is {salary}")

show_employee("Huzaifa", 10000)

# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]

def make_list(a, b, c, d):
    return [a, b, c, d]

print(make_list(4, 8, 10, 12))

# Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.

def km_to_miles(km):
    return km / 1.609

print(km_to_miles(932))

# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.

def is_divisible_by_11(number):
    return number % 11 == 0

print(is_divisible_by_11(23))

# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.

def get_highest(num1, num2):
    if num1 < num2:
        return num2
    return num1

print(get_highest(3, 6))

# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg and "fuel_per_liter" as optional arg that has default value to 280. The function should return the cost in Rs.

def fuel_cost(distance, fuel_per_liter=280):
    return distance * fuel_per_liter

print(fuel_cost(5))

# Write a function called is_valid_email  that takes an email address as an argument and returns True/False depending on whether it is a valid email address.
# Check rules:
# Must contain at least 1 character before the at symbol
# Must contain an @ symbol
# Must have at-least 1 character after the @ symbol and before the period(.)
# Must contain at least 1 character after the last period(.).
# Maximum 256 characters
# Must start with a letter or a number
# hint: use if statement 6 times to check each rule. if any one rule failed return false

def is_valid_email(email:str):
    is_valid = False
    if len(email) <= 256:
        is_valid = True
    else:
        return False

    if email[0] != "@":
        is_valid = True
    else:
        return False

    if "@" in email:
        is_valid = True
    else:
        return False

    if email[0].isalnum():
        is_valid = True
    else:
        return False

    add_symbol = email.find("@")
    dot_symbol = email[add_symbol:].find(".") + add_symbol
    if dot_symbol - add_symbol > 1:
        is_valid = True
    else:
        return False

    if len(email)-1 != dot_symbol:
        is_valid = True
    else:
        return False

    return is_valid

print(is_valid_email("huzaifa@g.com"))

