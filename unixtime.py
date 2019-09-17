#!/usr/bin/env pyhon

import datetime
from datetime import datetime
import time

print(int(time.time()))
print(time.time())

ds = 'August 20 2020'

dt2 = datetime.strptime(ds, '%B %d %Y')

print(dt2.date())

now = datetime.now()
print(now.isoformat())