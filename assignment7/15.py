# Create a function that takes a datetime object as input and formats it as "Month Day, Year" (e.g., "August 25, 2023") using strftime().

from datetime import datetime


date_str = input("Enter a date (DD/MM/YYYY): ")
date = datetime.strptime(date_str, "%d/%m/%Y")
new_format = date.strftime("%B %d, %Y")
print(new_format)