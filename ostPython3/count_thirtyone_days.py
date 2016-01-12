#!/usr/bin/env python3

from datetime import datetime, timedelta

now = datetime.now()
delta = timedelta(31)
date = now.strftime("%d")
delivery = now + delta
print("Today: %s" % now.strftime("%F"))
print("Delivery: %s" % delivery.strftime("%F"))
