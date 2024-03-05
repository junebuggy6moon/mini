#Q3
# Extend Bike and Fixie Classes
#- Add attributes `price` and `age` to the Bike class.
# You will need to change the constructor to include `price` and `age`.
#- Add a method `current_value` to the Bike class that returns the current value based on 20% depreciation p.a.
# cv = pp \times (1-dep)^{age}
# Create a new Fixie instance to test that the `current_value` is inherited.

class Bike:
    def __init__(self, name, size, price, age, front, rear_cassette):
        self.name = name
        self.size = size
        self.price = price
        self.age = age
        self.front = front
        self.rear_cassette = rear_cassette

class Fixie(Bike):
    def __init__(self, name, size, price, age, front, back):
        super().__init__(name, size, price, age, front, back)

    def current_value(self):
        dep_rate = 0.2
        current_value = self.price * (1 - dep_rate) ** self.age
        return current_value

fixie_bike = Fixie("Unknown_brand", "small", 1000, 1, 2, 3)
print("After depreciation price:", fixie_bike.current_value())

# Q4 Eleven_Speed Class
# Create a sub-class of Bike called Eleven_Speed for bikes that have an 11 speed rear cassette  and a single front chain cog. It will have attributes:
# - front (like the Fixie class)
# - rear_cassette: a list of cog sizes (like the Fixie class except a list)

# Because it will have 11 speeds (gears) it should have `get_top_gear` and `get_low_gear` methods. These are like the `get_gear` method in Fixie except the the `get_top_gear` method selects the smallest cog and `get_low_gear` selects the largest cog.
# - Create an instance of Eleven_Speed that has a 44 tooth front cog and these 11 rear cogs [11,13,15,17,19,22,25,28,32,36,42].
# - Show that the two new methods work for this instance.
# - Does `current_value` work?

# **Spoiler Altert**
# The low gear should be 44/42 $\approx$ 1.05.
# The top gear is 44/11 = 4.

class Eleven_Speed(Bike):
    def __init__(self, name, size, price, age, front, rear_cassette):
        super().__init__(name, size, price, age, front, rear_cassette)

    def get_top_gear(self):
        return self.front / min(self.rear_cassette)

    def get_lower_gear(self):
        return self.front / max(self.rear_cassette)

speed_changing_bike = Eleven_Speed("NewEra Bike", "Medium", 2000, 1, 44, [11, 13, 15, 17, 19, 22, 25, 28, 32, 36, 42])
print("Top gear ratio:", speed_changing_bike.get_top_gear())
print("Lower gear ratio:", speed_changing_bike.get_lower_gear())
