# Kenneth Linehan, 2022

# Write a program that outputs whether or not today is a weekday.

# Source used to help with code:
# https://www.codespeedy.com/how-to-find-day-name-from-date-in-python/

import datetime 
# Imports the datetime module to retrieve the date. Source: https://www.w3schools.com/python/python_datetime.asp
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# Sets up a variable with each day of week.
now = datetime.datetime.now().strftime('%A')
# Records a string representing the variable "now" %A means full weekday/weekend name
# FUrther info in regards how this works on - https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
if now in weekday:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
