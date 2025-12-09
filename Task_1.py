class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Child Class Lecturer:
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




# Child Class Analyst:
class Analyst(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



# Test
lecturer = Lecturer('Mark', 'Twain')
analyst = Analyst('Steven', 'Siegel')

print(isinstance(lecturer, Mentor))
print(isinstance(analyst, Mentor))
print(lecturer.courses_attached)
print(analyst.courses_attached)