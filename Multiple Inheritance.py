# multiple inheritance means derived class has multiple base class
# base class
class father:
    def gardenning(self):
        print("I like gardenning")


# base class
class mother:
    def travelling(self):
        print("I love travelling")


# derived class
class child(father, mother):
    def sports(self):
        print("I love sports")


c = child()
c.sports()
c.gardenning()
c.travelling()


# another way of multiple inheritance
class father:
    def skills(self):
        print("programming, ml")


class mother:
    def skills(self):
        print("art, teaching")


class child(father, mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print("sports")


c = child()
c.skills()
