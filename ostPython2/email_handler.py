#!/usr/bin/env python3
#
#
#       email_handler.py
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
This project calls for a function that takes an email address, a string,
and a list argument.  The function should return an email message addressed
to the email address passed as the first argument, with the second argument as
the message body.  If the list is non-empty, then each list item should be
treated as the name of a file and the corresponding file should be attached
(with an appropriate MIME type) to the message

Included are the files to attach in the same folder as the program.  While
it isn't necessary to send an email, simply uncommenting the sendMail()
function call in the main body of the program will accomplish this.  It is
designed to be run from my local linux box only, however.  So this will not run
on a machine that doesn't have sendmail on the localhost.  But the 
print(prepEmail(args)) will work just fine.  prepEmail() returns a msg object.

The companion test unittest utility is called testEmailHandler.py
"""

import smtplib
import os
import email, datetime, mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


lst = [
    'email-steampunk.txt',
    'steampunk.html',
    'blaster.jpg',
    'vaporizor.jpg']

types = [
        'text/html',
        'text/plain',
        'image/jpeg']

Msg = email.message_from_file(open(lst[0]))
astring = Msg.as_string()

def emailPrep(address, astring, lst):
    #msg = email.message_from_file(open(r'email-steampunk.txt')) # debugging
    msg = MIMEMultipart()
    msg['To'] = address
    msg['From'] = 'Steampunk Emporium <steampunk@localhost>'
    msg['Subject'] = 'New Blasters Available!'
    msg['Date'] = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S")

    for fn in lst:
        filetype = mimetypes.guess_type(fn)
        if types[0] in filetype: 
            textfile = open(fn, 'r')
            text = textfile.read()
            text_msg = MIMEText(text)
            msg.attach(text_msg)
            textfile.close()
        elif types[1] in filetype:
            textfile = open(fn, 'r')
            text = textfile.read()
            text_msg = MIMEText(text)
            msg.attach(text_msg)
            textfile.close()
        elif types[2] in filetype:
            jpgfile = open(fn, 'rb')
            img = MIMEImage(jpgfile.read())
            msg.attach(img)
            img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(fn))
        else:
            # useful for debugging...
            print(filetype, ": ",  types[0], types[1], types[2])
            print('file type not recognized')

    return msg
    #print(msg.as_string())  # for debugging...

def sendMail(msg):
    srv = smtplib.SMTP('localhost', 25)
    srv.sendmail(msg['From'], msg['To'], msg.as_string())
    srv.quit()


    
if __name__ == "__main__":
    tolist = [
            'deepbsd@yahoo.com',  # comment out for smtp 
            'deepbsd@gmail.com',  # comment out for smtp
            'deepbsd@earthlink',  # comment out for smtp
            'dsj@localhost', 
            'djackson@localhost'
            ]
    for address in tolist:
        print(emailPrep(address, astring, lst))
        #sendMail(emailPrep(address, astring, lst))
        
