#!/usr/bin/env python3
#
#
#          property_address.py
#
#    Lesson 12: Engineering Your Programs
#
#         by David S. Jackson
#             5/28/2015
#   
#    OST Python3: The Python Environment
#       for Kirby Urner, Instructor
#
"""
For Lesson 12, property_address.py adds command line parsing and external
configuration file reading to alter the behavior of the program in addition
to functionality from Lessons 10 and 11.

To import defaults from an external property_address.cfg file, comment out
lines 53 and 75.  To use internal static configs, uncomment those lines.

Note, I assumed it was necessary to maintain compatibility with functionality
from previous lessons, namely that ZIP unittests were 12345 and STATE unittests
were AB, not 12345-1234 and ABA respectively.  If I assumed wrong, this
behavior is easy to change by changing the @{state,zip_code}.{getter,setter}
regex check to re_ZIP_FMT and re_STATE_FMT, just as the cmd line validators
use. 
"""

import logging
import re
import argparse
import configparser




LOG_FILENAME = "property_address.log"
#LOG_FILENAME = "homework12.log"   
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s\n"
#LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s\n"
DEFAULT_LOG_LEVEL = "debug" 
LEVELS = { 'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
        }
re_STATE_FMT = "[A-Z]{2}$"  # default, unless overridden by external config
re_ZIP_FMT = "\d{5}$"   # default, unless overridden by external config


#"""    
# comment line above for reading external config file with 3 letter states
# and 10-digit zipcodes.  Also comment line 22 lines down...

config = configparser.RawConfigParser()
CONFIG_FILE = "property_address.cfg"
#global CONFIG_FILE = "V:/workspace/Python3_Lesson12/src/property_address.cfg"
config.read(CONFIG_FILE)
#logging.info("Reading external config file...")
for section in config.sections():
    for option in config.options(section):
        if section == 'log' and option == 'format':
            LOG_FORMAT = config.get(section, option)
        if section == 'log' and option == 'output':
            LOG_FILENAME = config.get(section, option)
        if section == 'validators' and option == 'zip_code':
            re_ZIP_FMT = config.get(section, option)
        if section == 'validators' and option == 'state':
            re_STATE_FMT = config.get(section, option)

# comment line below for reading external config file with 3 letter states
# and 10-digit zipcodes
#"""

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level"
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
    logging.info('Starting property_address.py program.')
    logging.debug("LOG_LEVEL = {}".format(level))
    logging.debug("LOG_FILENAME = {}".format(LOG_FILENAME))
    logging.debug("LOG_FORMAT = {}".format(LOG_FORMAT))
    logging.debug("re_STATE_FMT = {}".format(re_STATE_FMT))
    logging.debug("re_ZIP_FMT = {}".format(re_ZIP_FMT))
    try: 
        if CONFIG_FILE == 'property_address.cfg':
            logging.info("Reading configuration from external file...")
    except NameError:
        logging.info("Reading configuration from internal static variables...")

def validate_state(s):
    if re_STATE_FMT == '[A-Z]{3}$':
        msg = "State must contain 3 ALL CAP letters only."
    if re_STATE_FMT == '[A-Z]{2}$':
        msg = "State must contain only 2 CAP LETTERS only"
    if re.match(re_STATE_FMT, s):
        return s
    else:
        logging.error("Invalid cmd line STATE format given!")
        #raise StateError(msg)
        raise argparse.ArgumentTypeError(msg) 


def validate_zip(z):
    if re_ZIP_FMT == '\d{5}$':
        msg = "Zipcode must be in 12345 type format."
    if re_ZIP_FMT == '\d{5}\-\d{4}$':
        msg = "Zipcode must be in 12345-1234 type format."
    if re.match(re_ZIP_FMT, z):
        return z
    else:
        logging.error("Invalid cmd line ZIP_CODE format given!")
        #raise ZipCodeError(msg)
        raise argparse.ArgumentTypeError(msg)

class StateError(Exception): 
    "Custom exception for bad State input"
    def __init__(self, error):
        logging.error('STATE exception')
        self.error = error

class ZipCodeError(Exception): 
    "Custom exception for bad Zipcode input"
    def __init__(self, error):
        logging.error('ZIPCODE exception')
        self.error = error

class Address:

    def __init__(self, name, street_address, city, state, zip_code):
        logging.info('Creating a new address')
        self._name = name     
        self.address = street_address
        self.city = city
        self._state = state        
        self._zip_code = zip_code  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        msg = "Cannot reset existing name."
        logging.error("AttributeError raised: {}".format(msg))
        raise AttributeError('Cannot reset existing name.')

    @name.getter
    def name(self):
        logging.info('@name.getter triggered...')
        return self._name

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, name):
        logging.info('@state.setter triggered...')
        #if re.match('[A-Z]{2}$', name):
        if re.match(re_STATE_FMT, name):
            self._state = name
        else:
            raise StateError('Must have only 2 capital letters')

    @state.getter
    def state(self):
        #if re.match('[A-Z]{2}$', self._state):
        if re.match(re_STATE_FMT, self._state):
            return self._state
        else:
            raise StateError('Must have only 2 capital letters')

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.getter
    def zip_code(self):
        logging.info('@zip_code.getter triggered...')
        #if re.match('\d{5}$', str(self._zip_code)):
        if re.match(re_ZIP_FMT, str(self._zip_code)):
            return self._zip_code
        else:
            raise ZipCodeError('Must have 5 digit string.')

    @zip_code.setter
    def zip_code(self, value):
        logging.info('@zip_code.setter triggered...')
        #if re.match('\d{5}$', str(value)):
        if re.match(re_ZIP_FMT, str(value)):
            self._zip_code = value
        else:
            raise ZipCodeError('Must have 5 digit string.')





if __name__ == "__main__":

    """     -- uncomment for unittesting...
    start_logging()   # need to start logging ASAP...
    parser = argparse.ArgumentParser(description="Set attributes for and creates an Address Object")
    parser.add_argument('-l', 
            '--level', 
            dest="level", 
            choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
            default='DEBUG',
            help="sets default log level: DEBUG, INFO, WARNING, ERROR, or CRITICAL")
    parser.add_argument('-n', 
            '--name', 
            dest="name", 
            action="store", 
            required=True,
            help="sets name value of the Address object")

    parser.add_argument('-a', 
            '--address', 
            dest="address", 
            action="store", 
            required=True,
            help="Sets the street_address value of the Address object")

    parser.add_argument('-c', 
            '--city', 
            dest="city", 
            action="store", 
            required=True,
            help="Sets the city value of the Address object")

    parser.add_argument('-s', 
            '--state', 
            dest="state", 
            action="store", 
            required=True,
            type=validate_state,  
            help="Sets the state value of the Address object")

    parser.add_argument('-z', 
            '--zip_code', 
            dest="zip_code", 
            action="store", 
            required=True,
            type=validate_zip,  
            help="Sets the zip_code value of the Address object")


    
    args = parser.parse_args()
    start_logging(level=(args.level.lower())) # log with user-supplied level
    a = Address(args.name, args.address, args.city, args.state, args.zip_code)
    """   
    # uncomment above line for unittesting...



    
