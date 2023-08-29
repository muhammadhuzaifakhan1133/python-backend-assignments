# create a current datetime and then displays it in the format "HH:MM AM/PM"

from datetime import datetime


now = datetime.now()

print(now.strftime("%I:%M %p"))