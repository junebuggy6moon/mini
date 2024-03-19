# **Q** Change the month attribute so that it is a property.
# Code the setter function so that it produces a message if the month is not an integer between 1 and 12.

class my_date():
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    def show(self):
        print(self.day, '/', self.month, '/', self.year)

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if not isinstance(value, int):
            print("Error: Month must be an integer.")
            return
        if value > 12 or value < 1:
            print("Error: Month must be in between 1 and 12.")
        self._month = value

td = my_date(22, 8, 2018)
td.show()
td.month = 13
td.month = "JZ"




