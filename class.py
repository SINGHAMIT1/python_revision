# class is a paradigm of oop
# class is made of common set of properties and activities(which are called methods
# class=properties+methods
# object is nothing but a specific instance of a class.
class Human:
    # define properties
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    # define method do_work
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "play tennis")
        elif self.occupation == "actor":
            print(self.name, "do acts on films")

    # define another method do_speak
    def do_speak(self):
        if self.occupation == "tennis player":
            print(self.name, "says ,Hi, Let's play tennis")
        elif self.occupation == "actor":
            print(self.name, "says let's have some acting class tutorial")
    # end of entire class


# declare an instance of human class which is called object
tom = Human("Amit", "tennis player")
tom.do_speak()
tom.do_work()
