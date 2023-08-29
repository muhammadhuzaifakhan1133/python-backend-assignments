# Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.

from datetime import timedelta, datetime

date_str = input("Enter a date (DD/MM/YYYY): ")
days = int(input("Enter number of days to add: "))

date = datetime.strptime(date_str, "%d/%m/%Y")
date = date + timedelta(days=days)

print(date)
