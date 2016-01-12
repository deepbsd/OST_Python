#!/usr/bin/env python3
#
#
#       instrospect.py
#
#    Lesson 9: Uses of Instrospection
#
#     by David S. Jackson
#          8/4/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#

""" 
This module imports another module and makes a pretty print 'def
function()' declaration statement for each function and its respective
arguments.  Project description follows:


Project:

Write a program that imports a module and then goes through the module's
namespace to find any functions and print the names of the functions and their
arguments, in the same way as it might appear in a def statement.

Example output:

'def dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, **kw)'
'def dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, **kw)'
'def load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)'
'def loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)'

"""


import inspect
from pprint import pprint

# I chose the SMTP module...but you can change it to another easily...
#from smtplib import SMTP
#module = SMTP
#mod_string = 'SMTP'

#from threading import Thread
import csv

#module = Thread
module = csv
#mod_string = 'Thread'
mod_string = 'csv'

# slurp up the functions in the module
module_functions = inspect.getmembers(module, inspect.isfunction)


# make a pretty print 'def' line for each function in the module
for i in range(len(module_functions)):
    func = module_functions[i][0]
    myfunc =  mod_string+'.'+func
    myfunc = eval(myfunc)
    line = 'def ' + func + inspect.formatargspec(*inspect.getfullargspec(myfunc))
    pprint(line)
    

