#!/usr/bin/env python3

"""
Email message handling module: contains logic to store and retrieve
email messages using a MySQL relational database.
#!/usr/bin/env python3

"""
# remove this glob statement after testing
from glob import glob

from database import login_info
import mysql.connector as msc
from email import message_from_string
from email.utils import parsedate_tz, mktime_tz
from datetime import datetime, timedelta


conn = msc.Connect(**login_info)
curs = conn.cursor()

def store(msg):
    """
    Stores an email message, if necessary, returning its primary key.
    """ 
    message_id = msg['message-id']
    #text = msg.as_string()
    curs.execute("SELECT msgID FROM message WHERE msgMessageID=%s", (message_id, ))
    result = curs.fetchone()
    if result:
        return result[0]
    date = msg['date']
    dt = datetime.fromtimestamp(mktime_tz(parsedate_tz(date)))
    text = msg.as_string()
    curs.execute("INSERT INTO message (msgMessageID, imsgDate, msgText) VALUES (%s, %s)", (message_id, dt, text))
    conn.commit()
    curs.execute("SELECT msgID FROM message WHERE msgMessageID=%s", (message_id, ))
    return curs.fetchone()[0]

def msg_by_id(id):
    """
    Return the (presumably singleton) message whose primary key is given
    or raise KeyError if no such message exists.
    """
    curs.execute("SELECT msgID, msgText FROM message WHERE msgID=%s", (id, ))
    result = curs.fetchone()
    if  not result:
        raise KeyError("Id {0} not found in store".format(id))
    id, text = result
    msg = message_from_string(text)
    return id, msg

def msg_by_message_id(message_id):
    """
    Return the (presumably singleton) message whose "Message-ID" is given
    or raise KeyError if no such message exists.
    """
    curs.execute("SELECT msgID, msgText FROM message WHERE msgMessageID=%s", (message_id, ))
    result = curs.fetchone()
    if  not result:
        raise KeyError("Message-Id {0} not found in store".format(message_id))
    id, text = result
    msg = message_from_string(text)
    return id, msg

def msgs_by_date(mindate=None, maxdate=None):
    if not (mindate or maxdate):
        raise TypeError("Must provide at least one of mindate, maxdate")
    conds = []
    data = []
    if mindate:
        conds.append("msgDate >= %s")
        data.append(mindate)
    if maxdate:
        conds.append("msgdate < %s")
        data.append(maxdate+timedelta(days=1))
    sql = "SELECT msgid, msgText FROM message WHERE "
    sql += " AND ".join(conds)
    curs.execute(sql, tuple(data))
    result = []
    for id, text in curs.fetchall():
        result.append((id, message_from_string(text)))
    return result

### Trying to include specs to see if program runs alone without test.py

TBLDEF = """\
CREATE TABLE message (
     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
     msgMessageID VARCHAR(128),
     msgText LONGTEXT
)"""

FILESPEC = "testeml/*.eml"


if __name__ == "__main__":
    conn = msc.Connect(**login_info)
    curs = conn.cursor()
    print("doing login conn = {0} curs: {1}".format(conn, curs)) 
    print("about to execute table drop...")
    curs.execute("DROP TABLE IF EXISTS message")
    conn.commit()
    print("doing login conn = {0} curs: {1}".format(conn, curs)) 
    curs.execute(TBLDEF)
    conn.commit()
    files = glob(FILESPEC)
    msgids = {}
    message_ids = {}
    for f in files:
        ff = open(f)
        text = ff.read()
        msg = message_from_string(text)
        id = msgids[msg['message-id']] = store(msg)
        message_ids[id] = msg['message-id']

    curs.execute("DROP TABLE IF EXISTS message")
    conn.commit()
    print("All cleaned up.")
    print("bye bye")

