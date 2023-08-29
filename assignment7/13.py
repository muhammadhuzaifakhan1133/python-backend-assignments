# Create a function that takes a datetime object and a number of hours as input, then returns a new datetime object with the added hours.

from datetime import datetime, timedelta


def addHour(date:datetime, hours:int):
    return date + timedelta(hours=hours)
    
now = datetime.now()
future = addHour(now, 40)

print(future)