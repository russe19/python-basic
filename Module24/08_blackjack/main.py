import random


class Card:

    def __init__(self):
        self.suits = {1: 'Бубна', 2: 'Черва', 3: 'Пика', 4: 'Крести'}
        self.values = {1: 'Двойка', 2: 'Тройка', 3: 'Четверка', 4: 'Пятерка',
                       5: 'Шестерка', 6: 'Семерка', 7: 'Восьмерка', 8: 'Девятка',
                       9: 'Десятка', 10: 'Валет', 11: 'Дама', 12: 'Король', 13: 'Туз'}
        self.suit = random.randint(1, 4)
        self.suit = self.suits[self.suit]
        self.value = random.randint(1, 13)
        self.value = self.values[self.value]
        self.choice = 0


class Player:

    def __init__(self):
        self.point = 0
        self.summ = 0
        self.ace = 0
        self.defeat = False

    def give_card(self):
        self.card = Card()
        print(self.card.value, self.card.suit)
        if self.card.value == 'Двойка':
            self.point = 2
        elif self.card.value == 'Тройка':
            self.point = 3
        elif self.card.value == 'Четверка':
            self.point = 4
        elif self.card.value == 'Пятерка':
            self.point = 5
        elif self.card.value == 'Шестерка':
            self.point = 6
        elif self.card.value == 'Семерка':
            self.point = 7
        elif self.card.value == 'Восьмерка':
            self.point = 8
        elif self.card.value == 'Девятка':
            self.point = 9
        elif self.card.value == 'Десятка' or self.card.value == 'Валет' or self.card.value == 'Дама' or self.card.value == 'Король':
            self.point = 10
        elif self.card.value == 'Туз':
            self.point = 11
            self.ace += 1

    def add_card(self):
        self.summ += self.point
        if self.summ >= 21:
            if self.ace >= 1:
                self.ace -= 1
                self.summ -= 10
                print(self.summ)
                return self.summ
            else:
                return print('Игрок набирает больше 21 балла!')
        else:
            print(self.summ)
            return self.summ

    def choices(self):
        while True:
            self.choice = int(input('Взять еще одну карту? (0/1)'))
            if self.choice == 1:
                self.give_card()
                self.add_card()
                break
            elif self.choice == 0:
                break
            else:
                print('Ошибка ввода!')


def final_account(first, second):
    if first.summ > 21 and second.summ > 21:
        print('Оба игрока набрали больше 21 и проигрывают!')
    elif first.summ > 21:
        print('Игрок 1 набрал больше 21 и проигрывает!')
    elif second.summ > 21:
        print('Игрок 2 набрал больше 21 и проигрывает!')
    else:
        if first.summ > second.summ:
            print('Игрок 1 побеждает, так как он набрал больше баллов')
        elif second.summ > first.summ:
            print('Игрок 2 побеждает, так как он набрал больше баллов')
        else:
            print('Ничья')


play_1 = Player()
play_2 = Player()

play_1.give_card()
play_1.add_card()
play_1.give_card()
play_1.add_card()
play_1.choices()

play_2.give_card()
play_2.add_card()
play_2.give_card()
play_2.add_card()
play_2.choices()
final_account(play_1, play_2)
