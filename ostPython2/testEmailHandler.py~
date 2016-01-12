#!/usr/bin/env python3
#
#
#       testEmailHandler.py
#
#    Lesson 12: Handling Email
#
#     by David S. Jackson
#          3/21/2015
#   
#  OST Python2: Getting More Out of Python
#     for Pat Barton, Instructor
#
"""
This is the companion unittesting module for the email_handler.py program.
This program passes an email address and file contents as a body and also a
list of external files to check the performance of the email_handler.py
emailPrep function.  To avoid too many external files, the same files are used
as are used in the original function.  But they are passed to the function as
though they were different filenames and tested as though they were.

The headers are checked, but mainly the To: header is different.  The Subject
and from headers are the same as the email skeleton.  Finally, a msg.walk() is
performed to check that the multipart email content is as it should be.
"""
import unittest
from email_handler import emailPrep
import email
from email.mime.multipart import MIMEMultipart

class testEmailPrep(unittest.TestCase):

    def setUp(self):
        self.emailad = 'deepbsd@yahoo.com'
        self.efrom = 'Steampunk Emporium <steampunk@localhost>'
        self.substring = 'New Blasters Available!'
        self.lst = (
            'steampunk.html',
            'email-steampunk.txt',
            'blaster.jpg',
            'vaporizor.jpg')
        msg = email.message_from_file(open(self.lst[1]))
        self.string = msg.get_payload()



    def testEmailHdr(self):
        "Really, only the To: field is a good test..."
        msg = emailPrep(self.emailad, self.string, self.lst)
        self.assertEqual(msg.get('To'), self.emailad)
        self.assertEqual(msg.get('From'), self.efrom)
        self.assertEqual(msg.get('Subject'), self.substring)


    def testEmailContent(self):
        msg = emailPrep(self.emailad, self.string, self.lst)
        self.assertEqual(msg.get_content_type(), 'multipart/mixed')
        self.assertEqual(msg.is_multipart(), True)

    def testEmailPayload(self):
        typelst = ['text/plain', 'text/html', 'multipart/mixed', 'image/jpeg']
        msg = emailPrep(self.emailad, self.string, self.lst)
        for m in msg.walk():
            self.assertIn(m.get_content_type(), typelst)

    def testEmailBody(self):
        "Contents of email text (astring) file contained in msg"
        msg = emailPrep(self.emailad, self.string, self.lst)
        self.assertIn(self.string, msg.as_string())


    def tearDown(self):
        print('')
    




if __name__ == "__main__":
    unittest.main(warnings='ignore')
