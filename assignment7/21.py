# Write a program that takes a user-entered date in the format "MM/DD/YYYY" and prints it in the format "YYYY-MM-DD".

from datetime import datetime


date_str = input("Enter a date (MM/DD/YYYY): ")
date = datetime.strptime(date_str, "%m/%d/%Y")
print(date.strftime("%Y-%m-%d"))