# Create a program that takes a year and a month as input and prints the number of days in that month.
# without using calender module


def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = int(input("Enter year: "))
month = int(input("Enter month number (1-12): "))

days = mdays[month] + (month == 2 and isleap(year))
print(days)