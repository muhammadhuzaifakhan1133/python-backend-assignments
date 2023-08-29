# Create a program that calculates and prints the number of days remaining until a person's next birthday.

from datetime import datetime

dob_str = input("Enter your dob (dd/MM/YYYY): ")
dob_date = datetime.strptime(dob_str, "%d/%m/%Y")
current_date = datetime.now()
temp = datetime(current_date.year, dob_date.month, dob_date.day)
if (current_date.month > dob_date.month or (current_date.month == dob_date.month and current_date.day > dob_date.day)):
    temp = temp.replace(year=temp.year + 1)
remaining = temp - current_date
print("Remaing Days to your birthday is :", remaining.days)
