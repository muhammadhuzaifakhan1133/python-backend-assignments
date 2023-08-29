# Create a program that takes a date as string and returns the corresponding day of the week (e.g., Monday, Tuesday, etc.).

from datetime import datetime
import calendar

date_str = input("Enter a date (DD/MM/YYYY): ")
date = datetime.strptime(date_str, "%d/%m/%Y")
week_day = date.weekday()
week_name = calendar.day_name[week_day]
print(week_name)