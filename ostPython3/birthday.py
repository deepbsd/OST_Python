#!/usr/bin/env python3

import logging
from datetime import datetime
from optparse import OptionParser

logging.basicConfig(filename='birthday.log', level=logging.DEBUG)

class InvalidDateFormat(Exception):
    pass

def string_to_date(date):
    """
    Converts 'MM-DD-YYYY' to a datetime object or throws an InvalidDateFormat
    exception
    """
    try:
        # create a datetime object from the date value
        formatter_string = "%m-%d-%Y"
        birthday = datetime.strptime(date, formatter_string)
    except ValueError as e:
        # log the format error then raise it again so it can be handled
        # gracefully
        logging.error(e)
        raise InvalidDateFormat(e)
    return birthday

def birthday_counter(birthday):
    """
    Returns the number of days until your birthday.
    """
    now = datetime.now()
    birthday = string_to_date(birthday)
    logging.debug("birthday: %s" % birthday)

    # construct the upcoming birthday from this year, your birthday month, and
    # birthday day
    upcoming = datetime(now.year, birthday.month, birthday.day)
    logging.debug("upcoming: %s" % upcoming)

    # Make sure that upcoming is in the future, not the past
    if upcoming < now:
        upcoming = upcoming + timedelta(365)
        logging.debug("fixed upcoming: %s" % upcoming)

    # create a timedelta (duration) between the now and your birthday
    duration = upcoming - now
    logging.debug("duration: %s" % duration)

    # return only the days
    return duration.days

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-b', '--birthday',
            dest="birthday", 
            action="store",
            help="Your birthday in MM-DD-YYYY format")
    (options, args) = parser.parse_args()

    format_error_message = "birthday.py requires a date in MM-DD-YYYY format."
    if not options.birthday:
        parser.error(format_error_message)

    try:
        print(birthday_counter(options.birthday))
    except InvalidDateFormat:
        parser.error(format_error_message)


