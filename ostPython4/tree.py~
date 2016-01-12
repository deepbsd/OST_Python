#!/usr/bin/env python3


class Tree:
    def __init__(self, key):
        "Create a new Tree object with empty L & R subtrees."
        self.key = key
        self.left = self.right = None

    def insert(self, key):
        "Insert a new element into the tree in the correct position."
        if key < self.key:
            if self.left:
                self.left.insert(key)
            else:
                self.left = Tree(key)
        elif key > self.key:
            if self.right:
                self.right.insert(key)
            else:
                self.right = Tree(key)
        else:
            raise ValueError("Attempt to insert duplicate value")

    def walk(self):
        "Generate the keys from the tree in sorted order."
        if self.left:
            for n in self.left.walk():
                yield n
        yield self.key
        if self.right:
            for n in self.right.walk():
                yield n

if __name__ == "__main__":
    t = Tree("D")
    for c in "BJQKFAC":
        t.insert(c)

    print(list(t.walk()))
