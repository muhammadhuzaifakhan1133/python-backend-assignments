# Write a program that calculates and displays the number of days between two given dates.
from datetime import datetime

date1_str = input("Enter Date 1 (DD/MM/YYYY): ")
date2_str = input("Enter Date 2 (DD/MM/YYYY): ")

date1_obj = datetime.strptime(date1_str, "%d/%m/%Y")
date2_obj = datetime.strptime(date2_str, "%d/%m/%Y")

days = abs(date1_obj - date2_obj)
print(days)