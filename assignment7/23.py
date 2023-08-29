# Create a function that takes a timezone name as input and prints the current date time object in that timezone.

import pytz
from datetime import datetime

def apply_timezone(zone:str):
    try:
        tz_detail = pytz.timezone(zone)
        date = datetime.now()
        date = tz_detail.localize(date)
        return date
    except:
        print("Invalid zone")
        return None

print(apply_timezone("Asia/Karachi"))