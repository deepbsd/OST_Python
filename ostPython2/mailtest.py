#!/usr/bin/env python3

from glob import glob
from email import message_from_string
from database import login_info
import maildb
import unittest

import mysql.connector as DBC

conn = DBC.connect(**login_info)
curs = conn.cursor()


TBLDEF = """\
CREATE TABLE message (
    msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
    msgMessageID VARCHAR(128),
    msgText LONGTEXT
)"""

FILESPEC = "testeml/*.eml"

class testRealEmail_traffic(unittest.TestCase):
    def setUp(self):
        """
        Reads arbitrary number of email messages and stores them
        in a brand new message table.
        Destroys any previous table named message.
        """


        curs.execute("DROP TABLE IF EXISTS message")
        conn.commit()
        print("preparing for committing TBLDEF")
        curs.execute(TBLDEF)
        conn.commit()
        print("TBLDEF should be complete")
        print("preparing for globFILESPEC")

        files = glob(FILESPEC)
        self.msgids = {}
        self.message_ids = {}
        for f in files:
            ff = open(f)
            text = ff.read()
            msg = message_from_string(text)
            print("gonna store msg...")
            id = self.msgids[msg['message-id']] = maildb.store(msg)
            self.message_ids[id] = msg['message-id']
        print("maildb.store() run on messages, messages loaded...")
        print("cursor commit run...")
        

    def test_not_empty(self):
        """
        Make sure the setUp method created messages and loaded the table.
        """
        print("gonna test_not_empty")
        curs.execute("SELECT COUNT(*) FROM message")
        messagecount = curs.fetchone()[0]
        conn.commit()
        self.assertGreater(messagecount, 0, "Database message table is empty")

    def test_a_test(self):
        """
        Just try and get to this test and pass...
        """
        print("test_a_test...")
        self.assertEqual(1, 1)



if __name__ == "__main__":
    unittest.main(warnings='ignore')
