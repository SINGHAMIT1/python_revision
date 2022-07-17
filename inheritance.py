# car and bike classes are inherited from vehicle class
# parent class
class Vehicle:
    def general_usage(self):
        print("general use: transportation")


# children class
class car(Vehicle):
    def __init__(self):
        print("I am a car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific use : family travelling, long trip")


# children class
class bike(Vehicle):
    def __init__(self):
        print("I am a bike")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("specific use : personal use, short trip")


# creating object/instance of class
c = car()
c.general_usage()
c.specific_usage()
b = bike()
b.general_usage()
b.specific_usage()
print(isinstance(b,bike))
print(issubclass(car,Vehicle))
print(issubclass(bike,Vehicle))
print(issubclass(Vehicle,car))

