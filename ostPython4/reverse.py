#!/usr/bin/env python3
'''
class Reverse:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
'''

def Reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]


if __name__ == "__main__":

    rev = Reverse('onetwothreefour')

    for char in rev:
        print(char)
    data = 'onetwothreefour'
    print(list(data[i] for i in range(len(data)-1,-1,-1)))


