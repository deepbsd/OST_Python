#!/usr/bin/env python3
#
#
#        test_addarg.py
#
#    Lesson 7: Advanced Uses of Decorators
#
#     by David S. Jackson
#          7/29/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#

"""
Tests addarg function which should return list of args decorated function is
called with, prepended with the argument from the decorator.  Apparently, the
unittest case gets added already as args[0][0].  So, the test must test for
arg[0][0] and arg[0][2], since after the prepend, arg[0][1] is the
unittest.test function doing the call on the decorated function.  

There's probably a more elegant way to accomplish this, but this seems to work.
If I have to revisit this, then I have to revisit it.  We'll see...

The tests pass for now.
"""

from addarg import addarg 
import unittest


class TestAddArg(unittest.TestCase):

    """
    This tests the addarg function from addarg.py.  The @addarg decorator
    should be called with an argument, which then gets returned with the
    arguments for the function being decorated.  Examples below: function f1 is
    called with '1,2,3' as arguments, and the decorator @addarg is called with
    'one', then the addarg function should return ('one', 1, 2, 3) as the list
    of arguments that f1() was called with.
    """

    
    @addarg('one')
    def f1(*args, **kw):
        "Set up the first function.  Args will have 'one' prepended to them"
        #print("f1 called with:", args, kw)
        return args, kw
        
    @addarg('two')
    def f2(*args, **kw):
        "Set up second function.  Args will have 'two prepended to them"
        #print("f2 called with:", args, kw)
        return args, kw

    def test_f1(self):
        """
        Call f1(n) where n is range of 0..9  Must remove arg[0][1] from test
        case args.  For f1, @addarg('one') is used.
        """
        for n in range(10):
            args1 = self.f1(n)
            #print(args1)
            myargs1 = (args1[0][0], args1[0][2])
            self.assertEqual(myargs1, ('one', n))

    def test_f2(self):
        """
        Call f2(n) where n is range of 0..9  Must remove arg[0][1] from test
        case args.  For f2, @addarg('two') is used.
        """
        for n in range(20):
            args2 = self.f2(n)
            myargs2 = (args2[0][0], args2[0][2])
            self.assertEqual(myargs2, ('two', n))

    def test_sumall(self):
        @addarg(10)
        def sumall(*seq):
            return sum(seq)
        self.assertEqual(sumall(1,2,3), 16, "Not the right sum 10 + 1 + 2 + 3")

if __name__ == "__main__":
    unittest.main()


