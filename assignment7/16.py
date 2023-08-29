# Create a function that takes a datetime object as input and formats it as "Day-Month-Year" (e.g., "25-August-2023") using strftime().

from datetime import datetime


def formateDate(date:datetime):
    return date.strftime("%d-%B-%Y")

now = datetime.now()
print(formateDate(now))