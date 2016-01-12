#!/usr/bin/env python3

'''
Test the animal_farm animals
'''
import unittest
from animal_farm import Animal, Pig, Dog, Chicken

class Test(unittest.TestCase):

    def test_base_animal_class(self):
        "Tests the basics of the Animal class."
        animal = Animal("Orwell")
        self.assertRaises(NotImplementedError, animal.sound)
        self.assertFalse(animal.has_wings())

    def test_pig(self):
        "Tests the inhabitants of the farm"
        pig = Pig("Napoleon")
        self.assertEqual(pig.sound(), "oink!")
        self.assertFalse(pig.has_wings())

    def test_dog(self):
        dog = Dog("Bluebell")
        self.assertEqual(dog.sound(), "woof!")
        self.assertFalse(dog.has_wings())

    def test_chicken(self):
        chicken = Chicken("Kulak")
        self.assertEqual(chicken.sound(), "bok bok!")
        self.assertTrue(chicken.has_wings())

if __name__ == "__main__":
    unittest.main()


