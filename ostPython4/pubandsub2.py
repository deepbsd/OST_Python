#!/usr/bin/env python3
#
#
#        pubandsub2.py
#
#    Lesson 4: Publish and Subscribe
#
#     by David S. Jackson
#          7/21/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#
"""
Project:
    Modify the Subscriber.process() method so that the instance counts the
    number of times the method has been called.

    If after processing the current message, it has processed three messages,
    it should unsubscribe itself.

    Remove the unsubscribe code from the loop at the end of the main program,
    since it should no longer be necessary.

    Insert print() statements in your modified program until you think you have
    worked out why it no longer operates correctly, and see if you can suggest
    a way to fix it (whether or not you are able to implement your suggestion).

Second attempt.

Note: I went back to the earlier version of the code and updated it.  I
implemented the counter and self-unsubscribing behavior.  I also fixed the
problem of subscriber indexing changing in the middle of a loop and some
subscribers missing the broadcast or newsflash.  The fix was using a subscriber
dict instead of a list.  Now the publisher subscribes/unsubscribes the "bound method
SimpleSubscriber.process of Subscriber".

I think this meets the requirements of the assignment.  

Dave
"""

class Publisher:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, subscriber):
        print("+subscribing {} ".format(subscriber))
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)
        print("-{} unsubscribed...".format(subscriber))
    def publish(self, s):
        subscriber_dict = {}
        for subscriber in self.subscribers:
            subscriber_dict[str(subscriber)] = subscriber
        #print(subscriber_dict.values())
        #for subscriber in self.subscribers:
        for subscriber in subscriber_dict.values():
            subscriber(s)

if __name__ == '__main__':
    def multiplier(s):
        print("multiplier says: ", 2*s)

    class SimpleSubscriber:
        def __init__(self, name, publisher):
            self.processcount = 0
            self.name = name
            self.publisher = publisher
            publisher.subscribe(self.process)
        def process(self, s):
            self.processcount += 1
            if self.processcount > 3:
                print("#Processcount is {}, unsubscribing {}...".format(self.processcount, self.process))
                self.publisher.unsubscribe(self.process)
            else:
                print(self, ":", s.upper())
        def __repr__(self):
            return self.name

    publisher = Publisher()
    publisher.subscribe(multiplier)
    for i in range(6):
        newsub = SimpleSubscriber("Sub"+str(i), publisher)
        line = input("\n\nInput {}: ".format(i))
        publisher.publish(line)
        #if len(publisher.subscribers) > 3:
        #    publisher.unsubscribe(publisher.subscribers[0])



