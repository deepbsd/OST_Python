#!/usr/bin/env python3
#
#
#       math_quiz.py
#
#    Lesson 13: Time Computations
#
#     by David S. Jackson
#          6/4/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#
"""
Math_quiz.py gives the user a short, 5-question quiz in addition of two random
digits between 0 and 10.  It keeps track of whether the user gets the answer
right and also how long each question takes the user to answer.  The duration
of how long the quiz takes the user overall is recorded.  Accuracy is measured
in seconds only rather than microseconds.  If the user were to take two days to
answer five questions, the time would still be measured in seconds.

The time_it() function requires valid time objects as start and end inputs.  If
it does not receive them, a BadTimeObjError exception is raised.  

The time_it() function is tested by the test_math_quiz.py program.
"""

import random
from datetime import datetime, timedelta

class BadTimeObjError(Exception):
    "Custom Exception"
    pass

def gennum():
    "Generate a 'random' number between 1 and 10; return it"
    a = random.randint(1, 10)
    return a

def time_it(start, end):
    """Returns time in seconds between 'first' and 'second'. Both must be
    datetime objects"""
    try:
        elapsed = end - start
        return elapsed.seconds
    except:
        raise BadTimeObjError


def start_quiz():
    "Run the timer for a 5-question quiz that calls run_quiz()."

    # Containers for times and scores; start quiz timer...
    quiz_times = []
    quiz_scores = []
    quiz_start = datetime.now()

    # Get quiz inputs and start collecting times and scores...
    for count in range(0,5):
        firstnum = gennum()
        secondnum = gennum()
        answer = firstnum+secondnum
        question_start = datetime.now()
        feedback = input("What is the sum of {} and {}?  ".format(firstnum, secondnum)) 
        if int(feedback) == answer:
            print("{} is right!".format(feedback))
            quiz_scores.append("right")
        else:
            print("{} is wrong!  Correct answer is {}".format(feedback, answer))
            quiz_scores.append("wrong")

        question_end = datetime.now()
        quiz_times.append(time_it(question_start, question_end))

    # Total elapsed time for all quiz questions...
    quiz_end = datetime.now()
    total_quiztime = time_it(quiz_start, quiz_end)

    # Now print out summary of the quiz...
    for count in range(0,5):
        print("Question #{} took about {} seconds to complete and was {}".format(count+1, quiz_times[count], quiz_scores[count]))

    print("You took about {} seconds to finish the quiz".format(total_quiztime))
    # Total time to take the quiz is different from time just answering questions...
    print("Interestingly, the sum of the question times was only {} seconds".format(sum(quiz_times)))
    avg_time_per_question = float(total_quiztime/len(quiz_times))
    print("Your average time was {} seconds per question".format(avg_time_per_question))





if __name__ == "__main__":
    start_quiz()
