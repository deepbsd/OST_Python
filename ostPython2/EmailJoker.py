#!/usr/bin/env python3
#
#        EmailJoker.py
#
#      by David S. Jackson
#          on 4-9-2015
#       for OST, Python2, 
#          Lesson 13
#
#    Instructor:  Pat Barton
#
#
""" 
This program mails a joke of the day (JOTD) to a list of recipients
(RECIPIENTS) for a selected number of days (DAYCOUNT) starting at a 
spectific datetime.datetime object (STARTTIME).  These messages are 
saved in a mysql table.  Each day there are messages for each recipient 
for each day during DAYCOUNT.  Performance profiles for each number
of DAYCOUNTS will be given, both for 'fixed overhead' (the amount of
time required to generate the emails) and for 'variable overhead' 
(the amount of time to both create and store the emails in the 
database).  The idea is to figure out whether the total time is 
is more a product of fixed costs or of marginal costs.

This program includes a function to print times for all DAYCOUNTS
and compares the cost in time for just generating the emails compared
with both generating emails and storing them in a mysql database.

"""

import smtplib, email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message
from database import login_info
import mysql.connector as MSC
from datetime import datetime, timedelta
import time
import emailSettings


conn = MSC.Connect(buffered=True, **login_info)
#conn = MSC.Connect(**login_info)
curs = conn.cursor()

recip = emailSettings.RECIPIENTS
startime = emailSettings.STARTTIME
daycount = emailSettings.DAYCOUNT


TBLDEF = """\
CREATE TABLE jotd (
        msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
        msgDate DATETIME,
        msgRecipient VARCHAR(128),
        msgBody LONGTEXT
)"""


def gen_email(address, date, body):
    "Generates email messages. This would be a 'fixed cost'."
    msg = email.message.Message()
    #msg['Date'] = date.strftime("%F %T")
    msg['Date'] = date.strftime("%d %b %Y %H:%M:%S")
    msg['To'] = address
    msg['From'] = '<a href="mailto:website@example.com">website@example.com</a>'
    msg['Subject'] = "JOTD for {}".format(date.strftime("%F"))
    text = body
    msg.set_payload(text)
    return msg


def store_email(msg):
    "Stores an email message in a mysql table: a variable cost."
    sdate = msg['date']
    date = datetime.strptime(sdate, "%d %b %Y %H:%M:%S")
    recip1 = msg['to']
    body = msg.get_payload()

    curs.execute("""INSERT INTO jotd (msgDate, msgRecipient, msgBody) VALUES (%s, %s, %s)""", (date, recip1, body))
    conn.commit()
    curs.execute("SELECT * FROM jotd WHERE msgRecipient=%s", (recip1,))
    result = curs.fetchone()
    conn.commit()
    return result


def print_times():
    """
    prints the fixed and variable times for events based on various
    daycounts of duration
    """
    counts = [1, 10, 50, 100, 500]
    #counts = [1, 10, 50, 100]  # for debugging layout (500 takes loooong time!)

    print("\n\nDay  | Fixed Time | Variable Time | Total Time | Avg Time | DB % Email")
    print("Count|(Email Only)|  (DB-Fixed)   | (Email+DB) | per email| DB/Email  ")
    print("-----+------------+---------------+------------+----------+----------------")
    for c in counts:
        daycount = c
        # measure email only...
        e_start = time.time()
        populate_DB(daycount, email_only=True)
        e_end = time.time()
        e_duration = e_end - e_start
        # measure email+DB storage
        d_start = time.time()
        populate_DB(daycount)
        d_end = time.time()
        d_duration = d_end - d_start
        print("{0:>5}     {1:6.4f}     {2:9.4f}     {3:9.4f}  {4:9.4f}   {5:9.4f}".format(c, e_duration, d_duration-e_duration, d_duration, d_duration/(10*c), d_duration/e_duration))




    

def populate_DB(numofdays, email_only=False):
    """
    This used to be in the __main__ program.  After I tested it, I 
    wanted it out of the way so this program could be more flexible.
    If you *just* want fixed cost, set 'email_only=True'
    """
    jokefile = 'jokes.txt'

    daycount = numofdays
    jokeDB = []
    datelist = []
    day = startime
    curs.execute("DROP TABLE IF EXISTS jotd")
    conn.commit()
    curs.execute(TBLDEF)
    conn.commit()

    filehandle = open(jokefile, 'r')
    filetext = filehandle.readlines()
    filehandle.close()

    joke = ''
    jokeDB = []

    for line in filetext:
        if line != '%\n':
            joke += line
        else:
            jokeDB.append(joke)
            joke = ''

    #jokeDB = set(jokeDB)

    for d in range(0, daycount):
        datelist.append(day+timedelta(d))
    #for j in range(1, daycount+1):
        #jokeDB.append("joke"+str(j))

    for d in range(0, len(datelist)):
        date = datelist[d]
        joke = jokeDB[d]
        #print("Date: ", date, "D: ", d, "joke: ", joke)  #debugging
        for w in range(0, len(recip)):
            who = recip[w][1]
            if email_only:
                email = gen_email(who, date, joke)
            else:
                stored_email = store_email(gen_email(who, date, joke))


if __name__ == "__main__":
    #populate_DB(daycount)  # this was used for some debugging
    #whatever = store_email(gen_email(address, date, body))
    #print(whatever)
    print_times()  # use this to print a comparison of fixed and variable times
    
