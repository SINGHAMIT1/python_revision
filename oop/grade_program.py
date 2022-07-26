class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, maximum_students):
        self.name = name
        self.max_students = maximum_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grades(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("Bill", 19, 90)
s2 = Student("Jill", 19, 100)
s3 = Student("Nill", 19, 70)

course = Course("Science", 2)
course.add_students(s3)
course.add_students(s1)
print(course.add_students(s2))
print(course.students[0].name)
print(course.students[1].name)

print(course.get_average_grades())
