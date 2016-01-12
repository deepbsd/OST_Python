#!/usr/bin/env python3
#
#
#       pubandsub.py
#
#    Lesson 4: Publish and Subscribe
#
#     by David S. Jackson
#          7/20/2015
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


Note from student:  The biggest problem I had was making sense of the names of
each subscriber.  I changed the program so that actual names were given to the
subscribers, and at each input prompt, I said "first broadcast" or "second
broadcast" and so on.  I added print statements to the unsubscribe and subcribe
methods of publisher.  Now I can tell when a new subscriber is added or
removed.  When the processcount for a subscriber reaches 3, I am notified, and
I can see when the publisher.unsubscribe() method removes him from the
subscriber list.

I removed the multiplier(s) function and changed the publisher.publish() method
back to calling subscriber.process().  That seems to work ok.  I never did
think the multiplier() function added clarity.  Seems clearer to me without it.

The program could further be modified to execute more than simply 6 broadcast
messages to subscribers.  I could write a routine to dynamically generate names
to for each subscriber rather than exhaust a static list, but that's probably
beyond the point of this exercise at this point in time.

PROBLEM: The fourth broadcast skips "judy".  That is because, I think, "bob" is
unsubscribed and the list of self.subscribers gets shortened by one in the
middle of the for loop of for publishing the broadcasts.  Judy changes her
index in the list, and she doesn't get the fourth broadcast.  She does get the
fifth broadcast, however, and she is promptly unsubscribed as soon as she her
turn to get the fifth broadcast, which is her third broadcast.  

SOLUTION:  I think a different data structure for the subscribers is in order.
As a test of theory, I added a 'subscriber_dict' in the publish method, and
that structure was able to keep Judy from missing the fourth broadcast...

Dave

"""



class Publisher:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed.")
        self.subscribers.append(subscriber)
        print("Just subscribed {}".format(subscriber.name))
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)
        print("Unsubscribing {}".format(subscriber.name))
    def publish(self, s):
        subscriber_dict = {}
        for subscriber in self.subscribers:
            subscriber_dict[subscriber.name] = subscriber
        print(subscriber_dict.values())
        for subscriber in subscriber_dict.values():
            print("subscriber: {}".format(subscriber))
            #subscriber(s)   # I think it was clearer calling obj.process(s)
            subscriber.process(s)


if __name__ == '__main__':
    #def multiplier(s):
    #    print(2*s)

    class SimpleSubscriber:
        def __init__(self, name, publisher):
            self.processcount = 0  # initialize process count
            self.name = name
            self.publisher = publisher
            publisher.subscribe(self)

        def process(self, s):
            self.processcount += 1  # increment the process count
            if self.processcount > 3:
                #self.publisher.unsubscribe(multiplier(s)) # lose multiplier()!!!
                # tell the user who is being unsubscribed...
                print("{} must unsubscribe; process count is {}".format(self.name, self.processcount))
                self.publisher.unsubscribe(self)
            else:
                # subscriber hasn't hit 3 broadcasts yet; good to go...
                print(self.name, ":", s.upper())

        def __repr__(self):
            return self.name

    publisher = Publisher()
    # create some cute names for the subscribers...
    subscribernames = ["bob", "judy", "bill", "diane", "dino", "dom"]
    # again, don't need the multiplier function, seems to me...
    #publisher.subscribe(multiplier)
    for i in range(6):
        newsub = SimpleSubscriber(subscribernames[i], publisher)
        #newsub = SimpleSubscriber("Sub"+str(i), publisher)
        line = input("\n\nInput {}: ".format(i))
        publisher.publish(line)
        # unsbuscribe loop has been removed per assignment



