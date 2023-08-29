# Write a Python program that uses the date module to print the current date in the format "YYYY-MM-DD".

from datetime import date

today = date.today()

new_format = today.strftime("%Y-%m-%d")

print(new_format)