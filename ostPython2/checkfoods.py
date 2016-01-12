#!/usr/bin/env python3

"""
Check that all animals in zoo eat at least one food.
"""

import mysql.connector
from database import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

fmt = "{0:5} {1:15} {2:15}"
print(fmt.format("Animal_ID", "Name", "Feed"))
print("="*30)

cursor.execute("SELECT animal.id, name, feed FROM animal LEFT JOIN food ON animal.id=food.anid WHERE food.anid IS NULL")
for ID, name, feed in cursor.fetchall():
    print(fmt.format(ID, name, feed))


