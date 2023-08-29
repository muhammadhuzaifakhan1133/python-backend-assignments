# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

date_str = input("Enter Date MM/DD/YYYY :")
from datetime import datetime, date

date_obj = datetime.strptime(
    date_str,
    "%m/%d/%Y",
)

new_format = date_obj.strftime("%Y-%m-%d")
print(new_format)