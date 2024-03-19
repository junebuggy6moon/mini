# 1. Assuming the minumum wage is €9.25, set that as the default rate in the HourlyPaidEmployee class.
# Create a new hourly paid employee to show that this works.

class Employee():
    def __init__(self, name):
        self.name = name

class HourlyPaidEmployee(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)
        self.hours = 0
        self.rate = 9.25

    def set_hours(self, hours):
        self.hours = hours

    def set_rate(self, r):
        self.rate = r

    def get_pay(self):
        return self.rate * self.hours

jb = HourlyPaidEmployee("Joe Bloggs")
jb.set_hours(100)
jb.set_rate(9.25)

print(f"{jb.name} makes {jb.get_pay()} this week.")
