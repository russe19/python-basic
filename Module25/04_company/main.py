class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):

    def salary(self):
        pass


class Manager(Employee):

    def salary_calculation(self):
        salary = 13000
        return salary


class Worker(Employee):

    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.__hours = hours

    def get_hours(self):
        return self.__hours

    def salary_calculation(self):
        salary = 100 * self.get_hours()
        return salary


class Agent(Employee):

    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.__sales = sales

    def get_sales(self):
        return self.__sales

    def salary_calculation(self):
        salary = 5000 + self.get_sales() * 0.05
        salary = round(salary, 2)
        return salary


worker_1 = Worker('Саша', 'Петров', 25, 150)
worker_2 = Worker('Ваня', 'Иванов', 30, 200)
worker_3 = Worker('Полина', 'Носова', 24, 230)
manager_1 = Manager('Наташа', 'Волкова', 28)
manager_2 = Manager('Олег', 'Александров', 39)
manager_3 = Manager('Женя', 'Медведев', 44)
agent_1 = Agent('Дима', 'Зайцев', 36, 200000)
agent_2 = Agent('Коля', 'Кошкин', 21, 400000)
agent_3 = Agent('Софья', 'Боброва', 26, 440000)


def info(employee):
    print('Имя: {}\nФамилия: {}\nВозраст: {}\nЗарплата: {}\n'.format(employee.get_name(), employee.get_surname(),
                                                                     employee.get_age(), employee.salary_calculation()))


info(worker_1)
info(worker_2)
info(worker_3)
info(manager_1)
info(manager_2)
info(manager_3)
info(agent_1)
info(agent_2)
info(agent_3)
