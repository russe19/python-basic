import random


class Warrior():

    def __init__(self, index):
        self.health = 100
        self.index = index

    def damage(self):
        self.health -= 20


class Battle():

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def battle_war(self):
        while True:
            self.choise = random.randint(1, 2)
            if self.first.health == 0:
                print('Воин {} одерживает победу!'.format(self.second.index))
                break
            elif self.second.health == 0:
                print('Воин {} одерживает победу!'.format(self.first.index))
                break
            elif self.choise == 1:
                self.first.damage()
                print('Воин {} атаковал, у воина {} осталось {} здоровья'.format(self.second.index, self.first.index,
                                                                                 self.first.health))
            elif self.choise == 2:
                self.second.damage()
                print('Воин {} атаковал, у воина {} осталось {} здоровья'.format(self.first.index, self.second.index,
                                                                                 self.second.health))


war_1 = Warrior(1)
war_2 = Warrior(2)
batt = Battle(war_1, war_2)
batt.battle_war()
