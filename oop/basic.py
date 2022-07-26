class Dog:
    def __init__(self, name, age):  # parameters/arguments
        # attributes
        self.na = name
        self.ag = age

    # method 1
    def get_name(self):
        return self.na

    # method 2
    def get_age(self):
        return self.ag

    # method 3
    def modify_age(self, age):
        self.ag = age


d = Dog("Tom", 11)
print(d.get_name())
print(d.get_age())
d2 = Dog("Billo", 1)
print(d2.get_age())
print(d2.get_name())

d2.modify_age(23)
print(d2.get_age())
