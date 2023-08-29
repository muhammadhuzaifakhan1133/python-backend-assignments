# dt_named_and_short_form_format = "8-August-23 08:10:00"
# hint: https://strftime.org/

from datetime import datetime


date_str = "8-August-23 08:10:00"
date = datetime.strptime(date_str, "%d-%B-%y %H:%M:%S")
print(date)