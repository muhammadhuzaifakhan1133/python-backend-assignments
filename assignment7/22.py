# Create a function that takes a datetime object as input and displays the day of the week (e.g., "Monday") using strftime().
# hint: https://strftime.org/

from datetime import datetime


def week_of_date(date:datetime):
    return date.strftime("%A")

now = datetime.now()
print(week_of_date(now))