#!/usr/bin/env python3
#
#      testEmailJoker.py
#
#     by David S. Jackson
#         on 4-9-2015
#      for OST, Python2
#          Lesson 13
#
#   Instructor:  Pat Barton
#
"""
testEmailJoker.py tests for the correct number of unique dates,
the correct number of emails, the correct number of jokes,
and the correct starting and ending dates in the database.
"""

import mysql.connector as MSC
from database import login_info
import datetime
from datetime import timedelta
import unittest
import EmailJoker


conn = MSC.Connect(**login_info)
#conn = MSC.Connect(buffered=True, **login_info)
curs = conn.cursor()
startdate = datetime.datetime.today()
#startdate = datetime.date(2015, 4, 7)

TBLDEF = """\
CREATE TABLE jotd (
        msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
        msgDate DATETIME,
        msgRecipient VARCHAR(128),
        msgBody LONGTEXT
)"""

class testEmailJoker(unittest.TestCase):
    def setUp(self):
        """
        This method sets up a jotd table for each test; it uses
        only 2 mail recipients and a DAYCOUNT of 50.  Also, the
        jokes are a single word with a numeric suffix for easy
        comparison
        """
        curs.execute("DROP TABLE IF EXISTS jotd")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()

        self.starttime = datetime.datetime.today()
        day = self.starttime
        self.daycount = 50
        self.jokeDB = []
        self.datelist = []
        self.recipients = (
                ("bill", "bill@ourcompany.com"),
                ("teresa", "teresa@ourcompany.com")
                )
        for j in range(1, self.daycount+1):
            self.jokeDB.append("joke"+str(j))
        for d in range(0, self.daycount):
            self.datelist.append(day+datetime.timedelta(d))

        
        for d in range(0, len(self.datelist)):
            date = self.datelist[d]
            for w in range(0, len(self.recipients)):
                who = self.recipients[w][1]
                Msg = EmailJoker.gen_email(who, date, self.jokeDB[d])
                EmailJoker.store_email(Msg)



    def test_numOfDates(self):
        """
        This method tests the number of unique dates in the date 
        field of the DB
        """
        all_days = []
        expected = self.daycount
        curs.execute("SELECT msgDate FROM jotd")
        all_days = curs.fetchall()
        conn.commit()
        days = set(all_days)
        self.assertEqual(len(days), expected)

    
    def test_numOfEmails(self):
        """
        Total number of Emails in DB should equal 
        number of recipients * daycount
        This test also counts as a DB != Zero test also
        """
        expected = self.daycount * len(self.recipients)
        curs.execute("SELECT COUNT(*) FROM jotd")
        messagecount = curs.fetchone()[0]
        conn.commit()
        self.assertEqual(messagecount, expected)


    def test_numOfJokes(self):
        """
        This tests the Joke field of the database.  It counts
        the number of distinct jokes in the database.  That number
        should equal DAYCOUNT, one distinct joke for each day
        of the vacation.
        """
        all_jokes = []
        expected = self.daycount
        curs.execute("SELECT msgBody FROM jotd")
        all_jokes = curs.fetchall()
        jokes = set(all_jokes)
        joke_count = len(jokes)
        conn.commit()
        self.assertEqual(joke_count, expected)



    def test_dateRange(self):
        """
        This tests the range of dates in the headers.  
        That should start with STARTIME and end with
        STARTTIME + DAYCOUNT
        """
        all_dates = []
        expected_first = self.starttime.date()
        # for some reason, timedelta returns an extra day...
        expected_last = self.starttime + timedelta(self.daycount-1)
        expected_last = expected_last.date()
        curs.execute("SELECT msgDate FROM jotd")
        all_dates = curs.fetchall()
        conn.commit()
        first_date = all_dates[0][0]
        first_date = first_date.date()

        last_date = all_dates[-1][0]
        last_date = last_date.date()

        self.assertEqual(first_date, expected_first)
        self.assertEqual(last_date, expected_last)


if __name__ == "__main__":
    unittest.main()
