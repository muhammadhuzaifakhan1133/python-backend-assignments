# Write a program that calculates the time difference between two given datetime objects and displays it in hours, minutes, and seconds.

from datetime import datetime


date1_str = input("Enter a date 1 (DD/MM/YYYY HH:MM:SS): ")
date2_str = input("Enter a date 2 (DD/MM/YYYY HH:MM:SS): ")

date1 = datetime.strptime(date1_str, "%d/%m/%Y %H:%M:%S")
date2 = datetime.strptime(date2_str, "%d/%m/%Y %H:%M:%S")

days = abs(date1 - date2)

seconds = days.total_seconds()

hour = seconds // (60*60)
seconds = seconds % (60*60)
mints = seconds // 60
seconds = seconds % (60)

print("Hour:", hour)
print("Minute:", mints)
print("Seconds:", seconds)