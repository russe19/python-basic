import math

class Car:

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = 0.0175 * angle

    def __str__(self):
        return 'Координата x: {}\tКоордината y: {}\tУгол: {}'.format(self.x, self.y, self.angle * (1/0.0175))

    def move(self, distance):
        self.x += distance * math.cos(self.angle)
        self.y += distance * math.sin(self.angle)

    def turn(self, angle_turn):
        angle_turn *= 0.0175
        self.angle += angle_turn


class Bus(Car):

    def __init__(self, x, y, angle, passengers, money):
        super().__init__(x, y, angle)
        self.passengers = passengers
        self.money = money

    def __str__(self):
        return 'Координата x:{}\tКоордината y:{}\tУгол:{}\tКол-во пассажиров:{}\tДеньги:{}'.format(
            self.x, self.y, self.angle * (1/0.0175), self.passengers, self.money)

    def come_in(self):
        self.passengers += 1

    def come_of(self):
        self.passengers -= 1

    def move(self, distance):
        self.x += distance * math.cos(self.angle)
        self.y += distance * math.sin(self.angle)
        self.money += distance * self.passengers


print('Автомобиль')
car = Car(5, 6, 95)
print(car)
car.move(10)
print(car)
car.turn(75)
print(car)
car.move(10)
print(car)
print()
print('Автобус')
bus = Bus(5, 6, 95, 5, 100)
print(bus)
bus.come_in()
bus.come_in()
bus.move(20)
print(bus)
for _ in range(7):
    bus.come_of()
bus.turn(160)
bus.move(30)
print(bus)

