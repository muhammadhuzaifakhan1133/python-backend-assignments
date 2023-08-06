# Write a program to check if year is leap year.

# NOTE: search on google of what leap year is.

year = 2012

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Yes, It is leap year")
else:
    print("No, It is not leap year")