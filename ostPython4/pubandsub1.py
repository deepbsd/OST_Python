#!/usr/bin/env python3

class Publisher:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)
    def publish(self, s):
        for subscriber in self.subscribers:
            subscriber.process(s)


if __name__ == '__main__':
    class SimpleSubscriber:
        def __init__(self, publisher):
            publisher.subscribe(self)
            self.publisher = publisher
        def process(self, s):
            print(s.upper())

    publisher = Publisher()
    for i in range(3):
        newsub = SimpleSubscriber(publisher)
        line = input("Input {}: ".format(i))
        publisher.publish(line)
