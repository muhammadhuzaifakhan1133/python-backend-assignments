# Write a program that calculates the date and time of the daylight saving start in the year 2022.
# take timezone "US/Pacific"
# take string date as "2022-01-01 00:00:00"
# hint: use
# bool(tz_aware_dt.dst()) == True # dst activated
# bool(tz_aware_dt.dst()) == False # dst not activated

from datetime import datetime

import pytz


timezone = "US/Pacific"
date_str = "2022-04-01 00:00:00"
date = datetime.fromisoformat(date_str)
tz = pytz.timezone(timezone)
date = tz.localize(date)
print(date.dst())