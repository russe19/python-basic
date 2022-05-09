import random
import string


class Student:

    def __init__(self, index, FI='', group=0, performance=[]):
        self.FI = FI
        for i in range(2):
            self.FI += random.choice(string.ascii_letters).upper()
        self.group = random.randint(1, 5)
        self.performance = [random.randint(1, 5) for i in range(5)]
        self.gpa = 0
        self.index = index

    def info(self):
        print('ФИ:{}\nгруппа:{}\nУспеваемость:{}\n'.format(self.FI, self.group, self.performance))

    def average_score(self):
        for i_elem in self.performance:
            self.gpa += i_elem
        self.gpa /= len(self.performance)
        print('Средний балл {}: '.format(self.FI), self.gpa)


class Students:

    def __init__(self):
        self.students = [Student(index) for index in range(1, 11)]
        self.gpa_students = []

    def info(self):
        for i_elem in self.students:
            i_elem.info()

    def average_scores(self):
        for i_elem in self.students:
            i_elem.average_score()
            self.gpa_students.append(i_elem.gpa)
        print('\nСписок со средним баллом: ', self.gpa_students)

    def students_sort(self):
        self.gpa_sorted = []  # Функция sort не работала, поэтому пришлось сортировать через цикл
        for i in range(len(self.gpa_students)):
            self.gpa_sorted.append(min(self.gpa_students))
            self.gpa_students.remove(min(self.gpa_students))
        print('\nОтсортированный список со средним баллом: ', self.gpa_sorted)


# stud_1 = Student()
# stud_1.info()
# stud_1.average_score()
st_1 = Students()
st_1.info()
st_1.average_scores()
st_1.students_sort()
