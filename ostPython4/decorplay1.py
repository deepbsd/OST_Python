#!/usr/bin/env python3




class PetsAtHome:
    def __init__(self, name, alias):
        self.name = name
        self.alias = alias

    def printname(self):
        return self.name.upper()

    def printalias(self):
        return self.alias.upper()

def petrespect(pet):
    print("{} is a cool name, but {} is the alias!".format(pet.name.upper(), pet.alias.upper()))

if __name__ == "__main__":
    a = PetsAtHome("molly", "munchkin")
    b = PetsAtHome("milo", "loverboy")
    print("molly dict:", a.__dict__)
    print("milo dict:", b.__dict__)
    #print("method:",a.pa)
    petrespect(a)
    petrespect(b)
    c = a.printname()
    ca = a.printalias()
    print(a.name, a.alias)
    print(b.name, b.alias)
    print(c, ca, ";", b.printname(), b.printalias())
