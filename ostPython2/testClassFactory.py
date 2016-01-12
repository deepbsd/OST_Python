#!/usr/bin/env python3

import unittest
from classFactory import build_row

class DBTest(unittest.TestCase):
    
    def setUp(self):
        C = build_row("user", "id name email")
        self.c = C([1, "Steve Holden", "steve@holdenweb.com"])
        
    def test_attributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Steve Holden")
        self.assertEqual(self.c.email, "steve@holdenweb.com")
        
    def test_repr(self):
        self.assertEqual(repr(self.c), "user_record(1, 'Steve Holden', 'steve@holdenweb.com')")
        
    def test_retrieve(self):
        # set up curs here
        import mysql.connector
        from database import login_info
        db = mysql.connector.Connect(**login_info)
        curs = db.cursor()
        c = self.c.retrieve(curs, 'id=2')
        for value in c:
            #print(repr(value))
            self.assertEqual(repr(value), "user_record(2, 'Dave Jackson', 'deepbsd@yahoo.com')")
        
if __name__ == "__main__":
    unittest.main(warnings='ignore')

