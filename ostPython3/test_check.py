#!/usr/bin/env python3

import unittest
from checkteach import Teacher

class TestTeacher(unittest.TestCase):

    def setUp(self):
        self.teacher = Teacher("steve", "holden", "63", ["Python 3-1", "Python 3-2", "Python 3-3"], 5)

    def test_get(self):
        self.assertEqual(self.teacher.first_name, "Steve")
        self.assertEqual(self.teacher.last_name, "Holden")
        self.assertEqual(self.teacher.age, 63)
        self.assertEqual(self.teacher.classes, ["Python 3-1", "Python 3-2", "Python 3-3"])
        self.assertEqual(self.teacher.grade, "Fifth")
        self.teacher.description = "curmudgeon"
        self.assertEqual(self.teacher.description, "curmudgeon")
 

if __name__ == "__main__":
    unittest.main()
