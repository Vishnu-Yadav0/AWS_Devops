# os Module

'''
The os module provides a way of using operating system-dependent functionality like reading or writing to the file system.

'''
import os 

list_data = os.listdir('.')

#print(list_data)

"""
sys Module:

The sys module provides access to some variables used or maintained by the Python interpreter.

"""
import sys 

for i in sys.argv:
    print(i)


'''
re Module
The re module provides support for regular expressions.

Example: Finding all words in a string
'''

import re

text = "The rain in Spain falls mainly in the plain."
words = re.findall(r'\b\w+\b', text)
#print(words)

'''
datetime Module
The datetime module supplies classes for manipulating dates and times.

Example: Getting the current date and time


'''
from datetime import datetime

now = datetime.now()

print(now)