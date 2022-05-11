import random


class Person:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        self.satiety += 1
        self.house.food -= 1
        print('Вы поели!')

    def purchases(self):
        self.house.food += 1
        self.house.money -= 1
        print('Вы закупились продуктами!')

    def work(self):
        self.satiety -= 1
        self.house.money += 1
        print('Вы поработали!')

    def play(self):
        self.satiety -= 1
        print('Вы поиграли!')

    def one_day(self):
        self.number = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.purchases()
        elif self.house.money < 10:
            self.work()
        elif self.number == 1:
            self.work()
        elif self.number == 2:
            self.eat()
        else:
            self.play()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0


count_days = 0
my_house = House()
person_1 = Person('Саша', my_house)
person_2 = Person('Катя', my_house)
while True:
    person_1.one_day()
    person_2.one_day()
    if person_1.satiety > 0 or person_2.satiety > 0:
        count_days += 1
        print('Сытость: {}-{}, {}-{}, деньги: {}, еда:{}'.format(
            person_1.name, person_1.satiety, person_2.name, person_2.satiety, my_house.money, my_house.food))
    else:
        print('Вы проиграли!\nВы прожили {} дней'.format(count_days))
        break
