# Write a program that converts a given date time (tz aware) string from one timezone to another.

from datetime import datetime
from pytz import timezone


date_str = input("Enter a date (DD/MM/YYYY HH:MM:SS +00:00): ")
zone = input("Enter a zone in which you want to convert: ")

date = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S.%f%z")
print(date)
tz = timezone(zone)
date = date.astimezone(tz=tz)
print(date)
# America/Toronto
# 29/08/2023 16:43:06.548558+05:00