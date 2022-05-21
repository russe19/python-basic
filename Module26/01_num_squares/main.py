"""Класс-итератор"""


class Iterator_square:
    count = 0

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        Iterator_square.count = 0
        return self

    def __next__(self):
        if Iterator_square.count < self.number:
            Iterator_square.count += 1
            return Iterator_square.count ** 2
        else:
            raise StopIteration


number = 5
print('1-й способ:\n')
square = Iterator_square(number)
for i in square:
    print(i)

"""Функция-генератор"""


def generator_square(number):
    count = 0
    for i_elem in range(number):
        count += 1
        yield count ** 2


print('\n2-й способ:\n')
gen = generator_square(number)
for i in gen:
    print(i)

"""Генераторное выражение"""
print('\n3-й способ:\n')
generator = (i ** 2 for i in range(1, number + 1))
for i_elem in generator:
    print(i_elem)
