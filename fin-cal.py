"""
fin-cal.py: A simple program for financial events.
"""


class Data:
    # path = ?

    def backup_data(self):
        pass

    def restore_data(self):
        pass


class Event:

    def __init__(self, date, time, description, sentiment):
        self.date = date  # to store in proper form
        self.time = time  # consider format
        self.description = description
        self.sentiment = sentiment

    def __repr__(self):
        return f'{self.date}-{self.time}-{self.description}-{self.sentiment}'

    def __str__(self):
        return f'{self.date} during {self.time}: {self.description} ({self.sentiment})'
        # improve date display - consider formatting
        # provide for text descriptors (today, tomorrow, this week, next week)

    def add_event():
        pass

    def edit_event():
        pass

    def delete_event():
        pass

    def list_upcoming():
        pass

    def list_all():
        pass


class Web:
    def scrape():
        pass

    def notify():
        pass


event_test = Event('130821', 'POST', 'SOFI EARNINGS', 'BULLISH')
