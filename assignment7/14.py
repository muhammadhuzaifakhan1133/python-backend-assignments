# Write a program that takes a date string in the format "MM-DD-YYYY" as input and converts it to a datetime object using strptime().

from datetime import datetime


date_str = input("Enter a date (MM-DD-YYYY): ")
date = datetime.strptime(date_str, "%m-%d-%Y")
print(date)