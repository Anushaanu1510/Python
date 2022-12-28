import time
from datetime import datetime as dt
import datetime
time_obj = time.localtime()
current_time = time.strftime("%H:%M:%S", time_obj)
print("Current Date and Time is",current_time,"and",dt.date(dt.now()))
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))
