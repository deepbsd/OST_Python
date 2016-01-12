#!/usr/bin/env python3

"""
Read in and parse email messages to verify readability.

NOTE: This test creates the message table, dropping any previous
version and should leave it empty.  DANGER: this test will delete any existing
message table.
"""

from glob import glob
from email import message_from_string
import mysql.connector as msc
from database import login_info
import maildb
import unittest

conn = msc.Connect(**login_info)
curs = conn.cursor()

TBLDEF = """\
CREATE TABLE message (
     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
     msgMessageID VARCHAR(128),
     msgText LONGTEXT
)"""
#FILESPEC = "C:/PythonData/*.eml"
FILESPEC = "testeml/*.eml"

class testRealEmail_traffic(unittest.TestCase):
    def setUp(self):
        """
        Reads an arbitrary number of mail messages and
        stores them in a brand new message table.

        DANGER: Any existing message table WILL be lost.
        """
        #print("just about to drop table...")
        curs.execute("DROP TABLE IF EXISTS message")
        conn.commit()
        #print("table dropped")

        #print("just about to execute TBLDEF")
        #print("cursor: ", curs, " conn: ", conn)
        curs.execute(TBLDEF)
        conn.commit()
        #print("TBLDEF executed")
        #print("about to populate self.msgids and self.message_ids")
        files = glob(FILESPEC)
        self.msgids = {} # Keyed by message_id
        self.message_ids = {} # Keyed by id
        for f in files:
            ff = open(f)
            text = ff.read()
            msg = message_from_string(text)
            id = self.msgids[msg['message-id']] = maildb.store(msg)
            self.message_ids[id] = msg['message-id']
            #close(ff)  # try this out to remove warning
        print("last line of setUp()")

    def test_not_empty(self):
    #def skipTest(self):
        """
        Verify that the setUp method actually created some messages.
        If it finds no files there will be no messages in the table,
        the loop bodies in the other tests will never run, and 
        potential errors will never be discovered.
        """
        print("test not empty...")  # debugging
        curs.execute("SELECT COUNT(*) FROM message")
        messagect = curs.fetchone()[0]
        self.assertGreater(messagect, 0, "Database message table is empty")

    def test_message_ids(self):
    #def skipTest(self):
        """
        Verify that items retrieved by id have the correct Message-ID.
        """
        print("testing test_message_ids")  # debugging
        for message_id in self.msgids.keys():
            pk, msg = maildb.msg_by_id(self.msgids[message_id])
            self.assertEqual(msg['message-id'], message_id)

    def test_ids(self):
    #def skipTest(self):
        """
        Verify that items retrieved by message_id have the correct
        Message-ID.
        """
        print("testing test_ids...")
        for id in self.message_ids.keys():
            pk, msg = maildb.msg_by_message_id(self.message_ids[id])
            self.assertEqual(msg['message-id'], self.message_ids[id])
            #print(id)


if __name__ == "__main__":
    unittest.main(warnings="ignore")
