# class methods acts on the class itself not on the instances
# class attribute
class Person:
    no_of_people = 0  # class attribute

    def __init__(self, name):
        self.name = name
        Person.add_person()
        # Person.no_of_people += 1

    @classmethod  # decorator
    def no_of_people_(cls):
        return cls.no_of_people

    @classmethod
    def add_person(cls):
        cls.no_of_people += 1


p1 = Person("Tim")
# print(p1.no_of_people)
# Person.no_of_people = 99
p2 = Person("Jill")
# print(p2.no_of_people)
print(Person.no_of_people)
