class Parent:

    def __init__(self):
        self.name = input('Введите имя родителя: ')
        self.age = int(input('Введите возраст родителя: '))
        self.count_children = int(input('Введите количество детей: '))
        self.children = [Child(self.age) for _ in range(self.count_children)]
        self.children_name = []
        for my_child in self.children:
            self.children_name.append(my_child.name)
        self.feed_choice = 0
        self.calm_choice = 0

    def info_parents(self):
        print('\nИмя родителя:{}\nВозраст родителя:{}\nСписок детей:{}'.format(self.name, self.age, self.children_name))

    def feed_children(self):
        for my_child in self.children:
            if my_child.hungry == True:
                print('\nРебенок {} сыт'.format(my_child.name))
            else:
                print('\nРебенок {} голоден'.format(my_child.name))
                while True:
                    self.feed_choice = int(input('Покормить? (если 1 да, если 0 нет): '))
                    if self.feed_choice == 1:
                        my_child.feed()
                        break
                    elif self.feed_choice == 0:
                        break
                    else:
                        print('Ошибка ввода! ')

    def calm_down_children(self):
        for my_child in self.children:
            if my_child.calm == True:
                print('\nРебенок {} спокоен'.format(my_child.name))
            else:
                print('\nРебенок {} не спокоен'.format(my_child.name))
                while True:
                    self.feed_choice = int(input('Успокоить? (если 1 да, если 0 нет): '))
                    if self.feed_choice == 1:
                        my_child.calm_down()
                        break
                    elif self.calm_choice == 0:
                        break
                    else:
                        print('Ошибка ввода! ')


class Child:

    def __init__(self, age_par):
        self.age_par = age_par
        self.name = input('\nВведите имя ребенка: ')
        self.max_age_child = self.age_par - 16
        while True:
            self.age = int(input('Введите возраст ребенка: '))
            if self.age > self.max_age_child:
                print('Ошибка возраста! Попробуйте снова!')
            else:
                break
        while True:
            self.calm_ask = int(input('Ребенок спокоен? (если да ввести 1, если нет ввести 0): '))
            if self.calm_ask == 1:
                self.calm = True
                break
            elif self.calm_ask == 0:
                self.calm = False
                break
            else:
                print('Ошибка ввода!')
        while True:
            self.hungry_ask = int(input('Ребенок сыт? (если да ввести 1, если нет ввести 0): '))
            if self.hungry_ask == 1:
                self.hungry = True
                break
            elif self.hungry_ask == 0:
                self.hungry = False
                break
            else:
                print('Ошибка ввода!')

    def feed(self):
        self.hungry = True

    def calm_down(self):
        self.calm = True


p_1 = Parent()
p_1.info_parents()
p_1.feed_children()
p_1.calm_down_children()
