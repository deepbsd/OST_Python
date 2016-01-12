#!/usr/bin/env python3


import unittest

from teacher import Teacher


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

    def test_set(self):
        self.teacher.age = "21"
        self.assertEqual(self.teacher._age, 21)
        self.assertEqual(self.teacher.age, 21)
        self.assertRaises(ValueError, self.setAgeWrong)

    def setAgeWrong(self):
        self.teacher.age = "twentyone"

    def test_delete(self):
        del self.teacher.grade
        self.assertEqual(self.teacher.age, 64)
        self.assertRaises(AttributeError, self.accessGrade)

    def accessGrade(self):
        return self.teacher.grade

if __name__ == "__main__":
    unittest.main()



