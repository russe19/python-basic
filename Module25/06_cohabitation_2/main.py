import random


class Person:

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def eat(self):
        self.satiety += 10
        self.house.food -= 10
        self.house.all_food += 10

    def pet(self):
        self.happiness += 5
        self.satiety -= 10


class Husband(Person):

    def __init__(self, name, house):
        super().__init__(name, house)
        self.satiety = 30
        self.happiness = 100

    def work(self):
        self.satiety -= 10
        self.house.money += 150
        self.house.all_money += 150
        print('Вы поработали!')

    def play(self):
        self.satiety -= 10
        self.happiness += 20
        print('Вы поиграли!')

    def one_day_husband(self):
        if self.satiety < 30:
            self.eat()
        elif self.house.money < 400:
            self.work()
        elif self.happiness < 30:
            self.pet()
        else:
            self.play()


class Wife(Person):

    def __init__(self, name, house):
        super().__init__(name, house)
        self.satiety = 30
        self.happiness = 100

    def product_buy(self):
        self.house.food += 40
        self.house.cat_food += 20
        self.house.money -= 60
        self.satiety -= 10
        print('Вы закупились продуктами!')

    def product_coat(self):
        self.house.money -= 350
        self.happiness += 60
        self.satiety -= 10
        self.house.all_coat += 1

    def cleaning(self):
        if self.house.dirt < 100:
            self.house.dirt = 0
        else:
            self.house.dirt -= 100

    def one_day_wife(self):
        if self.satiety < 30:
            self.eat()
        elif self.house.food < 50:
            self.product_buy()
        elif self.house.dirt > 100:
            self.cleaning()
        elif self.happiness < 70:
            self.pet()
        elif self.house.money > 500:
            self.product_coat()
        else:
            self.eat()


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 30
        self.house = house

    def eat_cat(self):
        self.satiety += 20
        self.house.food -= 10
        self.house.all_food += 10
        print('Кот поел!')

    def sleep(self):
        self.satiety -= 10

    def tear_wallpaper(self):
        self.house.dirt += 5
        self.satiety -= 10
        print('Дерет обои!')

    def one_day_cat(self):
        number = random.randint(1, 2)
        if self.satiety < 30:
            self.eat_cat()
        else:
            if number == 1:
                self.tear_wallpaper()
            else:
                self.sleep()


class House:
    all_money = 0
    all_food = 0
    all_coat = 0

    def __init__(self):
        self.food = 50
        self.money = 100
        self.cat_food = 30
        self.dirt = 30


count_days = 0
my_house = House()
husband = Husband('Саша', my_house)
wife = Wife('Катя', my_house)
cat = Cat('Барсик', my_house)
while True:
    husband.one_day_husband()
    wife.one_day_wife()
    cat.one_day_cat()
    if my_house.dirt > 90:
        husband.happiness -= 10
        wife.happiness -= 10
    if husband.happiness < 10 or wife.happiness < 10 or husband.satiety < 0 or wife.satiety < 0 or cat.satiety < 0:
        print('Вы програли!\nВы прожили {} дней'.format(count_days))
        break
    elif count_days >= 365:
        print('Поздравляем! Вы прожили год')
        print('Сытость:\t{}:{}\t{}:{}\t{}:{}\nСчастье:\tСаша:{}\tКатя:{} \nДеньги:\t{}\tЕда:{}\tГрязь:{}'.format(
            husband.name, husband.satiety, wife.name, wife.satiety, cat.name, cat.satiety,
            husband.happiness, wife.happiness, my_house.money, my_house.food, my_house.dirt))
        break
    else:
        count_days += 1
        print('Вы прожили', count_days, 'дней')
        print('Сытость:\t{}:{}\t{}:{}\t{}:{}\nСчастье:\tСаша:{}\tКатя:{} \nДеньги:\t{}\tЕда:{}\tГрязь:{}'.format(
            husband.name, husband.satiety, wife.name, wife.satiety, cat.name, cat.satiety,
            husband.happiness, wife.happiness, my_house.money, my_house.food, my_house.dirt))
