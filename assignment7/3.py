# Write a program that takes a birth year as input and calculates the age of a person.

from datetime import datetime

dob_str = input("Enter your date of birth (dd/MM/YYYY): ")
dob_date = datetime.strptime(dob_str, "%d/%m/%Y")
current_date = datetime.now()
age =  current_date - dob_date
years = round(age.days / 365, 1)
print(years)