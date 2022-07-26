# general class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Hi! I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")


# specific classes
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # calling the upper level parent class
        self.color = color

    def speak(self):
        print("Meaoow")

    def show(self):
        print(f"Hi! I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


# Instance
p = Pet("Tim", 19)
p.show()
c = Cat("Mim", 10, "Brown")
c.show()
d = Dog("Rin", 1)
d.show()
f = Fish("Rocky", 12)
c.speak()  # overwrite mother class
d.speak()  # overwrite mother class
f.show()
