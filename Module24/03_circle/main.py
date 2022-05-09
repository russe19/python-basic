import math


class Round():

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def info(self):
        print('Координата x:{}\nКоордината y:{}\nРадиус окружности:{}'.format(self.x, self.y, self.r))

    def area_of_circle(self):
        self.area = math.pi * (self.r ** 2)
        print('Площадь круга равна ', self.area)

    def perimeter_of_circle(self):
        self.perimeter = 2 * math.pi * self.r
        print('Периметр круга равна ', self.perimeter)

    def increase(self):
        self.k = float(input('Во сколько раз увеличить круг? '))
        self.r *= math.sqrt(self.k)
        print('Увеличенный радиус: ', self.r)


class Flat:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def intersection(self):
        if self.first.r + self.second.r >= math.sqrt(
                math.pow((abs(self.first.x - self.second.x)), 2) + math.pow((abs(self.first.y - self.second.y)), 2)):
            print('Окружности пересекаются')
        else:
            print('Окружности не пересекаются')


round_1 = Round(0, 0, 3)
round_2 = Round(6, 0, 2)
round_1.area_of_circle()
round_1.perimeter_of_circle()
round_1.increase()
round_1.info()
flat_1 = Flat(round_1, round_2)
flat_1.intersection()
