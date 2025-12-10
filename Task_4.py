# --- Классы ---

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    def __str__(self):
        avg = self._average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress) or 'Нет'
        finished_courses = ', '.join(self.finished_courses) or 'Нет'
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg}\n"
            f"Курсы в процессе изучения: {courses_in_progress}\n"
            f"Завершенные курсы: {finished_courses}"
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() < other._average_grade()

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        if course not in self.courses_in_progress:
            return 'Ошибка'
        if course not in lecturer.courses_attached:
            return 'Ошибка'
        if not (0 <= grade <= 10):
            return 'Ошибка'
        lecturer.grades.setdefault(course, []).append(grade)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    def __str__(self):
        avg = self._average_grade()
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {avg}"
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() < other._average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'


# --- Функции ---

def average_grade_students(students, course):
    """Средняя оценка за домашние задания по курсу"""
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0


def average_grade_lecturers(lecturers, course):
    """Средняя оценка за лекции по курсу"""
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0


# Студенты
student1 = Student('Jenifer', 'Lopez', 'f')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']

student2 = Student('Mike', 'Tyson', 'm')
student2.courses_in_progress = ['Python', 'C++']
student2.finished_courses = ['Алгоритмы']

# Лекторы
lecturer1 = Lecturer('James', 'Lebron')
lecturer1.courses_attached = ['Python', 'Git']

lecturer2 = Lecturer('Jessica', 'Alba')
lecturer2.courses_attached = ['Python', 'C++']

# Проверяющие
reviewer1 = Reviewer('Kate', 'Beckinsale')
reviewer1.courses_attached = ['Python']

reviewer2 = Reviewer('Jet', 'Lee')
reviewer2.courses_attached = ['Git', 'C++']

# Студенты оценивают лекторов
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Git', 8)
student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'C++', 9)

# Проверяющие оценивают студентов
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student1, 'Git', 7)
reviewer2.rate_hw(student2, 'C++', 8)

# --- Вывод ---
print("--- Студенты ---")
print(student1)
print()
print(student2)
print("\n--- Сравнение студентов ---")
print(f"student1 < student2: {student1 < student2}")

print("\n--- Лекторы ---")
print(lecturer1)
print()
print(lecturer2)
print("\n--- Сравнение лекторов ---")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")

print("\n--- Проверяющие ---")
print(reviewer1)
print()
print(reviewer2)

# --- Проверка функций ---
print("\n--- Средние оценки по курсам ---")
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print(f"Средняя оценка студентов по курсу 'Python': {average_grade_students(students_list, 'Python')}")
print(f"Средняя оценка лекторов по курсу 'Python': {average_grade_lecturers(lecturers_list, 'Python')}")