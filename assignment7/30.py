# Booking System
# Design a booking system where users specify a start datetime, end datetime, and timezone. Implement a function that checks whether a specified time slot is available.
# if timeslot is available then store the start_date and end_date in the list of objects i.e
"""
booking_storage = [
  {
    "start_date": "",
    "end_date": ""
  }
]
"""
# hint 1: store dates in booking_storage in UTC format i.e pytz.utc
# hint 2: use for loop, the loop should run 5 times. ask user input inside the loop

# instruction to test your program:
# first iteration of loop
# give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone

# second iteration of loop
# give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00" as end_date and "Asia/Riyadh" as timezone
# above program should not accept this booking as the slot is already booked by the first iteration

from datetime import datetime

import pytz


booking_storage = []

is_valid = True
for i in range(5):
    print("Booking for USER %d" %(i+1))
    is_valid = True
    start_date_str = input("Enter booking start date (DD/MM/YYYY HH:MM:SS): ")
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y %H:%M:%S")
    end_date_str = input("Enter booking end date (DD/MM/YYYY HH:MM:SS): ")
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y %H:%M:%S")
    zone = input("Enter time zone name: ")
    tz = pytz.timezone(zone)
    start_date = tz.localize(start_date)
    start_date = start_date.astimezone(pytz.utc)
    end_date = tz.localize(end_date)
    end_date = end_date.astimezone(pytz.utc)
    for booking in booking_storage:
        if (booking["start_date"] < start_date and start_date < booking["end_date"]) or (booking["start_date"] < end_date and end_date < booking["end_date"]) :
            is_valid = False
            break
    if (not is_valid):
        print("Booking for USER %d cannot be successfully save due to inavailability of time slots" %(i+1))
        continue
    else:
        booking_storage.append({
            "start_date": start_date,
            "end_date": end_date,
        })
        print("Booking saved successfully")
    print(booking_storage)