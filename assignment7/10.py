# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

from datetime import datetime


date_str = input("Enter a date (MM/DD/YYYY): ")
date = datetime.strptime(date_str, "%m/%d/%Y")

print(date.strftime("%Y-%m-%d"))