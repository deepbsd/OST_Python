#!/usr/bin/env python3
#
#
#       inputter.py
#
#    Lesson 9: Reading and 
#       Writing Files
#
#     by David S. Jackson
#         12/1/2014
#   
#  OST Python1: Beginning Python
#     for Pat Barton, Instructor
#
"""
 Lesson 9 Objective.  Use while loop to accept input from the user 
 (<enter> to exit the program).  Save the input to a file and then print it.
 Upon starting the program will display any previous content of the file.
"""

usr_file = open('obj_inputter.txt', 'r')
usr_file.close()

while True:
    #file_contents = open('obj_inputter.txt','r').readline()
    file_contents = open('obj_inputter.txt','r').read()
    print(file_contents)
    usr_file.close()
    usr_file = open('obj_inputter.txt','a')
    usr_input = input('<ENTER> to end or \n Enter text: ')
    if not usr_input:
        usr_file.close()
        print("Bye now!")
        break
    usr_file.write(usr_input)
    usr_file.close()

print()



