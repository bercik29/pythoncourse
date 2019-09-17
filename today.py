#!/usr/bin/env pyhon

import datetime
from datetime import date
import time

today  = date.today()

print('Current year: ', today.year)
print('Current month: ', today.month)
print('Current day: ', today.day)
print('Current weekday: ', today.weekday()+1)

print(today.isocalendar())

print(today)
print(dir(today))

now = datetime.datetime.now()
print(now)

print(datetime.datetime.utcnow())

dob = datetime.datetime(1963, 12, 18)
print(dob)

today = datetime.date.today()
print(now)

dob = now + datetime.timedelta(days = 60)
print(dob)
print(dob.weekday()+1)