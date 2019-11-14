from datetime import *
import datetime
import time
time_one = datetime.time(1, 2, 3)
print("Time One :: ", time_one)

time_two = datetime.time(hour=23, minute=59, second=59, microsecond=99)
print("Time Two :: ", time_two)

date_one = datetime.date(month=3, year=2019, day=31)
print("Date One :: ", date_one)

today = datetime.date.today()
print("Today :: ", today, today.timetuple())

print("Difference Between Time :: ", timedelta(time_two.second) - timedelta(time_one.second))
print("Today :: ", datetime.date.today())

print("Time.asctime() :: ", time.asctime())
now = time.gmtime()
print("time.asctime(time.gmtime) :: ", time.asctime(now))

start = time.time()
time.sleep(3)
stop = time.time()
print(stop - start)