# Design a program that helps schedule a meeting across different timezones. The program should take the meeting time in one timezone and display the corresponding times in other timezones.
# consider three countries: UK, US, Saudi Arab and Pakistan
# consider the meeting time is: 30 August 2023 at 2 PM Pakistan time

from datetime import datetime

import pytz


date = datetime(2023, 8, 30, 14, tzinfo=pytz.timezone("Asia/Karachi"))

# UK: Europe/London
# US: US/Central
# Saudi Arab: Asia/Riyadh
# Pakistan: Asia/Karachi

uk_date = date.astimezone(tz=pytz.timezone("Europe/London"))
print("In UK, meeting will be held on: ", uk_date)

us_date = date.astimezone(tz=pytz.timezone("US/Central"))
print("In US, meeting will be held on: ", us_date)

saudi_date = date.astimezone(tz=pytz.timezone("Asia/Riyadh"))
print("In Saudia Arab, meeting will be held on: ", saudi_date)

pk_date = date.astimezone(tz=pytz.timezone("Asia/Karachi"))
print("In Pakistan, meeting will be held on: ", pk_date)