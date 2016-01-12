#!/usr/bin/env python3

"""
commands.py: Parse logging level options from sys.argv
"""

from optparse import OptionParser

if __name__ == "__main__":

    # instantiate an OptionParser object
    parser = OptionParser()
    parser.add_option("-l", "--loglevel", 
        action="store",
        dest="level",
        default="warning",
        help="set level of logger: debug, info, warning (default), error, critical")
    (options, args) = parser.parse_args()
    print("level: %s" % options.level)
