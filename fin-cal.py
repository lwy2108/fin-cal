"""
fin-cal.py: A simple program to track financial events.
"""

import datetime as dt
import re


class Data:
    # path = ?

    def backup_data(self):
        pass

    def restore_data(self):
        pass


class Event:

    def __init__(self, datetime, est_time, description, sentiment):
        self.datetime = dt.datetime.strptime(datetime, '%d-%m-%y %H:%M')
        self.est_time = est_time
        self.description = description
        self.sentiment = sentiment

    def __repr__(self):
        return f'{self.date}-{self.time}-{self.description}-{self.sentiment}'

    def __str__(self):
        return f'{self.date} during {self.time}: {self.description} ({self.sentiment})'
        # improve date display - consider formatting
        # provide for text descriptors (today, tomorrow, this week, next week)

    def add_event(self):
        pass

    def edit_event(self):
        pass

    def delete_event(self):
        pass

    def list_upcoming(self):
        pass

    def list_all(self):
        pass


class Web:
    def scrape(self):
        pass

    def notify(self):
        pass


print('Please enter event date (DD-MM-YY):')
event_date = input() # validate date
print('Time if available (HH:MM):')
event_time = input()  # fix on empty

# validate time (testing)
if re.match('^[0-9]{2}:[0-9]{2}$', event_time):
    print('Match')
else:
    print('Fail')

event_datetime = '{} {}'.format(event_date, event_time)
print(event_datetime)

# event_test = Event(event_datetime, 'POST', 'SOFI EARNINGS', 'BULLISH')
# print(event_test.datetime)
# print(event_test.est_time)
