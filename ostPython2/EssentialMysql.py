#!/usr/bin/env python3

import mysql.connector as msc

USERNAME = "djackson"
PASSWORD = "2d33p4m32"
login_info = {
        'host': "localhost",
        'user': USERNAME,
        'password': PASSWORD,
        'database': USERNAME,
        'port': 3306
        }

conn = msc.Connect(**login_info)
curs = conn.cursor()
print('curs is: ', curs, 'conn is: ', conn)
print('trying to drop a table')
curs.execute("DROP TABLE IF EXISTS message")
print('table dropped')
