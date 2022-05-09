class Water:

    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()


class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()


class Earth:

    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()


class Storm:

    def __init__(self):
        self.name = 'Шторм'


class Dirt:

    def __init__(self):
        self.name = 'Грязь'


class Dust:

    def __init__(self):
        self.name = 'Пыль'


class Lightning:

    def __init__(self):
        self.name = 'Молния'


class Lava:

    def __init__(self):
        self.name = 'Лава'


class Steam:

    def __init__(self):
        self.name = 'Пар'


a = Air()
b = Fire()
c = a + b
print(c.name)
