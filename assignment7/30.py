# Booking System
# Design a booking system where users specify a start datetime, end datetime, and timezone. Implement a function that checks whether a specified time slot is available.
# if timeslot is available then store the start_date and end_date in the list of objects i.e
"""
booking_storage = [
  {
    "car_model": "", # corolla, civic

    "start_date": "",
    "end_date": ""
  }
]
"""
# hint 1: store dates in booking_storage in UTC format i.e pytz.utc
# hint 2: use for loop, the loop should run 5 times. ask user input inside the loop

# instruction to test your program:
# first iteration of loop
# give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone and car_model 

# second iteration of loop
# give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00" as end_date and "Asia/Riyadh" as timezone  and car_model 
# above program should not accept this booking as the slot is already booked by the first iteration

#You must write the following functions

#add_tz() # this should convert naive date to tz_awre
#convert_tz() # this should convert date from one tz to another
#is_slot_available() # this should return True or False
#book_the_car() # this should add the detail in booking_storage

#I didn't mention what info you need to pass to the above functions. Its part of your assigment to pass info to the function and return the value from function.

from datetime import datetime

import pytz


def add_tz(naive_dt: datetime, zone: str):
    tz = pytz.timezone(zone)
    tz_aware_dt = tz.localize(naive_dt)
    return tz_aware_dt

def convert_tz(tz_aware_dt: datetime, zone: str):
    tz = pytz.timezone(zone)
    new_tz_aware_dt = tz_aware_dt.astimezone(tz)
    return new_tz_aware_dt

def is_slot_available(bookings: list, start_tz_aware_dt: datetime, end_tz_aware_dt: datetime):
    for booking in bookings:
        if (booking["start_date"] < start_tz_aware_dt and start_tz_aware_dt < booking["end_date"]) or (booking["start_date"] < end_tz_aware_dt and end_tz_aware_dt < booking["end_date"]) :
            return False
    return True

def book_the_car(bookings: list, start_tz_aware_dt: datetime, end_tz_aware_dt: datetime):
    bookings.append({
            "start_date": start_tz_aware_dt,
            "end_date": end_tz_aware_dt,
        })
    print("Booking saved successfully")

booking_storage = []

is_valid = True
for i in range(5):
    print("Booking for USER %d" %(i+1))
    start_datetime_str = input("Enter booking start date (DD/MM/YYYY HH:MM:SS): ")
    start_datetime = datetime.strptime(start_datetime_str, "%d/%m/%Y %H:%M:%S")
    end_datetime_str = input("Enter booking end date (DD/MM/YYYY HH:MM:SS): ")
    end_datetime = datetime.strptime(end_datetime_str, "%d/%m/%Y %H:%M:%S")
    zone = input("Enter time zone name: ")
    start_tz_aware_datetime = add_tz(start_datetime, zone)
    end_tz_aware_datetime = add_tz(end_datetime, zone)
    new_start_tz_aware_datetime = convert_tz(start_tz_aware_datetime, "UTC")
    new_end_tz_aware_datetime = convert_tz(end_tz_aware_datetime, "UTC")
    if is_slot_available(booking_storage, new_start_tz_aware_datetime, new_end_tz_aware_datetime) :
       book_the_car(booking_storage, new_start_tz_aware_datetime, new_end_tz_aware_datetime)
    else:
        print("Booking for USER %d cannot be successfully save due to inavailability of time slots" %(i+1))
    print(booking_storage)