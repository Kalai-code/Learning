# base class
class Vehicle():
    def description(self):
        print("I'm a Vehicle!")

# subclass
class Car(Vehicle):
    def description(self):
        print("I'm a Car!")

# create an object from each class
v = Vehicle()
c = Car()

v.description()
c.description()

# base class
class Vehicle():
    def __init__(self, color):
        self.color = color
    def description(self):
        print("I'm a", self.color, "Vehicle")

# subclass
class Car(Vehicle):
    def __init__(self, color, style):
        super().__init__(color)    # invoke Vehicle’s __init__() method
        self.style = style
    def description(self):
        print("I'm a", self.color, self.style)

# create an object from each class
v = Vehicle('Red')
c = Car('Black', 'SUV')

v.description()
# Prints I'm a Red Vehicle
c.description()
# Prints I'm a Black SUV
