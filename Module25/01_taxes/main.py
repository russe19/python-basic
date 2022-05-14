class Property:

    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        pass


class Apartment(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        tax = self.worth / 1000
        print('Налог на квартиру равен ', tax)
        return tax


class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        tax = self.worth / 200
        print('Налог на автомобиль равен ', tax)
        return tax


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        tax = self.worth / 500
        print('Налог на дачу равен ', tax)
        return tax


class Interface:

    def __init__(self):
        self.money = int(input('Введите кол-во денег пользователя: '))
        self.worth = int(input('Введите стоимость имущества: '))
        self.choice = int(input('Введите тип имущества (Квартира - 1 / Машина - 2 / Дача - 3): '))

    def lack(self):
        need_money = self.tax - self.money
        if need_money > 0:
            print('Не хватает {} для оплаты налога'.format(need_money))
        else:
            self.money -= self.tax
            print('Налог оплачен, осталось {} денег'.format(self.money))

    def choices(self):
        if self.choice == 1:
            self.tax = Apartment(self.worth).tax()
            self.lack()
        elif self.choice == 2:
            self.tax = Car(self.worth).tax()
            self.lack()
        elif self.choice == 3:
            self.tax = CountryHouse(self.worth).tax()
            self.lack()
        else:
            print('Неверный ввод')


Interface().choices()
