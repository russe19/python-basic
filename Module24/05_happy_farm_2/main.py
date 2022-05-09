class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая', }

    def __init__(self, index):
        self.index = index
        self.state = 0

    def info_potato(self):
        print('Картошка {} на стадии {}'.format(self.index, Potato.states[self.state]))

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.info_potato()

    def it_ripe(self):
        if self.state == 3:
            return True
        return False


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка проростает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if all([i_potato.it_ripe() for i_potato in self.potatoes]):
            return True
        else:
            return False


class Gardener:

    def __init__(self, garden):
        self.name = input('Введите имя садовника: ')
        self.garden = garden

    def care(self):
        print('\n{} ухаживает за грядкой'.format(self.name))
        self.garden.grow_all()
        if self.garden.are_all_ripe():
            self.harvest()

    def harvest(self):
        for i_potato in self.garden.potatoes:
            i_potato.state = 0
        print('{} выкопал всю картошку на грядке'.format(self.name))


my_gardener = Gardener(PotatoGarden(5))
my_gardener.garden.are_all_ripe()
for _ in range(6):
    my_gardener.care()
