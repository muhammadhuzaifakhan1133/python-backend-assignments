from datetime import datetime, date, time

# current date

# current_date = date.today()
# print(current_date)

# print(current_date.year)
# print(current_date.month)
# print(current_date.day)

# with detail

# current_date_time = datetime.now()
# print(current_date_time)
# print(current_date_time.year)
# print(current_date_time.month)
# print(current_date_time.day)
# print(current_date_time.hour)
# print(current_date_time.minute)
# print(current_date_time.second)

# print(type(current_date))
# print(type(current_date_time))


# create date time from integer or from string

# from integer

# my_day = 26
# my_month = 8
# my_year = 2023
# d = date(year=my_year, month=my_month, day=my_day)
# print(d)
# print(d.year)


# from string (ISO Format)

# dt_iso = "2023-08-26" # iso format
# dt = "26-08-2023" # not iso format
# dt = "2023/08/23" # not iso format

# dt_obj = date.fromisoformat(dt_iso)
# print(dt_obj.year)

# valid iso format
# datetime_str = "2023-08-26 10:56:44"
# dt_obj = datetime.fromisoformat(datetime_str)
# print(dt_obj)
# print(dt_obj.month)


# from timestamp

# ts = 1693029240
# ts_date = datetime.fromtimestamp(ts)
# print(ts_date.year)

# from sring (NOT ISO FORMAT)

# dt_pk = "26-08-2023"
# dt_us = "08/26/2023"
# invalid_dt = "2023/-08-- /26"
# dt_iso = "2023-08-26"

# dt = datetime.strptime(
#     dt_pk,
#     "%d-%m-%Y"
# )

# dt = datetime.strptime(
#     dt_us,
#     "%m/%d/%Y",
# )

# dt = datetime.strptime(
#     invalid_dt,
#     "%Y/-%m-- /%d",
# )

# print(dt.year)


# dt = datetime.now()
# x = str(dt)
# print(x) # 2023-08-26 11:31:20.297265
# iso_date = datetime.strptime(
#     x,
#     "%Y-%m-%d %H:%M:%S.%f"
# )
# print(iso_date.year)


# dt = "2023-08-26 11:31:20.297265"
# dt_obj = datetime.fromisoformat(dt)
# print(dt_obj.year)
# x = dt_obj.replace(year=2024)
# print(x.year)

# NO NEED TO SPECIFY FORMAT BUT IT IS RISKY
# from dateutil import parser
# x = "2023/02/01"
# dt_obj = parser.parse(x)
# print(dt_obj.year)


# TIMEDELTA

from datetime import timedelta

# x = date.today()
# print(x)
# x = x - timedelta(days=2)
# print(x)

# x = datetime.fromisoformat("2023-08-05")
# for i in range(1,10):
#     changed_date = x - timedelta(days=i)
#     # changed_date = x.replace(day=x.day-i) # NOT SUITABLE FOR THIS CASE
#     print(changed_date)


# current_dt = datetime.now()
# custom_dt = datetime.now()
# custom_dt = custom_dt.replace(day=2)
# print(current_dt)
# print(custom_dt)
# diff = current_dt - custom_dt
# print(diff)
# print(diff.days)
# print(diff.total_seconds())
# print(diff.total_seconds() / (60*60))  # total hour


# import calendar
# info = calendar.monthrange(year=2023, month=7)
# # return (week day of first day of month, last date of month)
# print(info)

import pytz
# print(datetime.now()) # 2023-08-26 12:39:46.410402
# current_d = datetime.now(tz=pytz.timezone("Asia/Karachi"))
# print(current_d) # 2023-08-26 12:39:46.551699+05:00

# playing with timezone

tz_detail = pytz.timezone("US/Pacific")

dt_str = "2020-03-07 15:00:00"
dt_obj= datetime.fromisoformat(dt_str)

tz_aware_dt = tz_detail.localize(dt_obj)
print(tz_aware_dt) # 2020-03-07 15:00:00-08:00

dt_str = "2020-03-08 15:00:00"
dt_obj= datetime.fromisoformat(dt_str)

tz_aware_dt = tz_detail.localize(dt_obj)
print(tz_aware_dt)


# change timezone of timzone aware date

print(tz_aware_dt.astimezone(pytz.timezone("Asia/Karachi")))
