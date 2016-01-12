#!/usr/bin/env python3

"""
Email message handling module: contains logic to store and retrieve
email messages using a MySQL relational database.
"""

from database import login_info
import mysql.connector as msc
from email import message_from_string

conn = msc.Connect(**login_info)
curs = conn.cursor()

def store(msg):


    message_id = msg['message-id']
    text = msg.as_string()
    curs.execute("SELECT msgID FROM message WHERE msgMessageID=%s", (message_id, ))
    result = curs.fetchone()
    conn.commit()
    if result:
        return result[0]
    curs.execute("INSERT INTO message (msgMessageID, msgText) VALUES (%s, %s)", (message_id, text))
    #conn.commit()
    curs.execute("SELECT msgID FROM message WHERE msgMessageID=%s", (message_id, ))
    returnthingie = curs.fetchone()[0]
    conn.commit()
    return returnthingie


