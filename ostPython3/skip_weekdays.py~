#!/usr/bin/env python3

from datetime import datetime, timedelta

delivery = datetime.now()
delta = timedelta(1)
count = 0
while count < 31:
    delivery = delivery + delta
    if delivery.isoweekday() in (6, 7):
        continue
    count += 1


now = datetime.now()
print("Now:", now)
print("Delivery:", delivery)
print("Today: %s" % now.strftime("%d"))
print("Delivery: %s" % delivery.strftime("%d"))
