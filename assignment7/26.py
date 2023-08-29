# Create a function that takes a timezone name and a number of hours as input, and prints the current time plus the specified hours in that timezone

from datetime import datetime, timedelta
import pytz


zone = input("Enter zone name: ")
hours = int(input("Enter number of hours you want to add: "))

tz = pytz.timezone(zone)
now = datetime.now()
now = tz.localize(now)

now = now + timedelta(hours=hours)

print(now)