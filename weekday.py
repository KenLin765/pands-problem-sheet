# Kenneth Linehan

# Write a program that outputs whether or not today is a weekday.

# Sources:
# https://www.codespeedy.com/how-to-find-day-name-from-date-in-python/

import datetime
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
now = datetime.datetime.now().strftime('%A')
if now in weekday:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
