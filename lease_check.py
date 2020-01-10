# lease check
import datetime
import pytz

TOTAL = 10000.0 #miles
PERDAY = 10000.0/365.0 #miles/day
STARTED = 185.0 #miles
STARTDATE =  datetime.datetime(2019, 11, 9, 0, 0, tzinfo=pytz.UTC)
NOW = datetime.datetime.now(pytz.utc)
DIFF = NOW - STARTDATE # how long have had car
DAYS = DIFF.days
print("MILES YOU ARE ALLOWED THUS FAR: ")
MILES_ALLOWED = (PERDAY * DAYS) + STARTED
print(int(MILES_ALLOWED))


