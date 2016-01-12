#!/usr/bin/env python3

"""
animal.py: a class to represent an animal in the database
"""

class Animal:

    def __init__(self, id, name, family, weight):
        self.id = id
        self.name = name
        self.family = family
        self.weight = weight

    def __repr__(self):
        return "Animal({0}, '{1}', '{2}', {3})".format(self.id, self.name, self.family, self.weight)


if __name__ == "__main__":
    import mysql.connector
    from database import login_info
    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()
    cursor.execute("SELECT id, name, family, weight FROM animal")
    animals = [Animal(*row) for row in cursor.fetchall()]
    from pprint import pprint
    pprint(animals)


