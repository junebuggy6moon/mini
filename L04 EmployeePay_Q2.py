# 2. Update the SalariedEmployee class to cover the concept of a part-time worker, i.e. a salaried employee
# working three days a week would be paid 60% of the full salary.
# **Hint:** SalariedEmployee should probably have an $__init__$ function now.
# Use the one from HourlyPaidEmployee as a template.
class Employee():
    def __init__(self, name):
        self.name = name

class SalariedEmployee(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)

    def set_salary(self, sal):
        self.salary = sal

    def set_part_time_pct(self, pct):
        self.pct = pct

    def get_pay(self):
            return self.salary * (self.pct / 100)

mm = SalariedEmployee("Marvelous Mary")
mm.set_part_time_pct(60)
mm.set_salary(100000)

print(f"{mm.name} made {mm.get_pay()} last year.")



