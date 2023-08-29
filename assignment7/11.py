# Create a function that takes a datetime in the format "MM/DD/YYYY HH:MM:SS" as string  formats it as "YYYY-MM-DD HH:MM:SS".

from datetime import datetime


date_str = input("Enter a date (MM/DD/YYYY HH:MM:SS): ")
date = datetime.strptime(date_str, "%m/%d/%Y %H:%M:%S")

print(date.strftime("%Y-%m-%d %H:%M:%S"))