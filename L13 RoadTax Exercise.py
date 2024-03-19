# Road Tax Exercise
# In Ireland, the price you pay for road tax is based on two different assessments;
# engine size: manufactured before July 2008,
# Co2 emissions: manufactured after July 2008.
#
# Here is a subset of both price models
#
# ### CO2 Model
#
# |**Price**  | **CO2** |
# |-----------|---------|
# |€120       |0 -   1  |
# |€170       |2 -   80 |
# |€180       |81 - 100 |
# |€190       |101 - 110|
# |€200       |111 - 120|

#
# ### Engine CC
# |**Price** |**CC** |
# |----------|-------|
# |€199 |   0 - 1000|
# |€299 |1001 - 1100|
# |€330 |1101 - 1200|
# |€358 |1201 - 1300|
# |€385 |1301 - 1400|
#
# 1. Create classes `Car`, and subclasses `PreJul2008` and `PostJul2008`.
# The subclasses have a method `get_tax_rate`.
# `PreJul2008` has an attribute `CC`
# `PostJul2008` has an attribute `CO2`
#
# 2. Write a function `total_tax` that will take a list of car objects as argument and return
# the total tax bill for these cars. Test it on a fleet with two pre July 2008 cars (1250CC and 1400CC)
# and a post July 2008 car with an emission level of 110.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class PreJul2008(Car):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model,)
        self.engine_cc = engine_cc

    def get_tax_rate(self):
        if self.engine_cc <= 1000:
            return 199
        if self.engine_cc <= 1100:
            return 299
        if self.engine_cc <= 1200:
            return 330
        if self.engine_cc <= 1300:
            return 358
        if self.engine_cc <= 1400:
            return 385

class PostJul2008(Car):
    def __init__(self, brand, model, co2_emissions):
        super().__init__(brand, model)
        self.co2_model = co2_emissions

    def get_tax_rate(self):
        if self.co2_model <= 1:
            return 120
        if self.co2_model <= 80:
            return 170
        if self.co2_model <= 100:
            return 180
        if self.co2_model <= 110:
            return 190
        if self.co2_model <= 120:
            return 200

def total_tax(cars):
    return sum(car.get_tax_rate() for car in cars)

car1 = PreJul2008("Nissan", "Sentra", 1250)
car2 = PreJul2008("Audi", "Q5", 1400)
car3 = PostJul2008("Tesla", "S3", 110)

fleet = [car1, car2, car3]

print("Total tax €", total_tax(fleet))