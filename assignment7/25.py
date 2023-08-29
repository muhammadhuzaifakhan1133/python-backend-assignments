# Write a program that takes a datetime object (naive) and a timezone name as input, and returns a localized datetime object in the specified timezone.

from datetime import datetime

import pytz


date_str = input("Enter a date (DD/MM/YYYY HH:MM:SS): ")
zone = input("Enter a zone name: ")

date = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
tz = pytz.timezone(zone)

date = tz.localize(date)

print(date.astimezone(pytz.timezone("Asia/Karachi")))