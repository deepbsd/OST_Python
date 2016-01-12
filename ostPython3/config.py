#!/usr/bin/env python3


import configparser


# create a config parser object
config = configparser.RawConfigParser()

# open and read the addressbook.cfg file into the config parser
config.read('addressbook.cfg')

# loop through the sections
for section in config.sections():
    print(section)
    # get all the options for the current section
    for option in config.options(section):
        #print the option and its value indented for clarity
        text = '    %s = %s' % (option, config.get(section, option))
        print(text)
