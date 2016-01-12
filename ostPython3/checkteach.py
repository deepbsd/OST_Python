#!/usr/bin/env python3

class Teacher(object):

    grades = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth"}

    def __init__(self, first_name, last_name, age, classes, grade):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.age = int(age)
        self.classes = sorted(classes)
        self.grade = self.grades[grade]
