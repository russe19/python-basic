import functools
import datetime
from typing import Callable


def logging(func: Callable) -> Callable:
    @functools.wraps(func)  # NOTE здесь можно использовать такой синтаксис декораторов
    def inner_function(*args, **kwargs) -> None:
        try:
            func(*args, **kwargs)
        except Exception as err:
            time = datetime.datetime.now()
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                # NOTE уточнить кодировку при работе с файлом никогда не лишне
                file.write('{},{} - {}\n'.format(time, func.__name__, err))

    return inner_function


@logging
def find_number(numbers: list) -> None:
    """
    Функция на поиск чисел.
    :param numbers:
    :return:
    """
    for i_elem in numbers:
        result = i_elem / 1
        print(i_elem)


numbers = [2, 3, 'f', 8]


@logging
def test(num_1: int, num_2: int) -> None:
    # NOTE можно поправить оформление и содержание документации
    '''
    Деление числа.
    :param num_1:
    :param num_2:
    :return:
    '''
    result = num_1 / num_2
    print(num_1, ' / ', num_2, ' = ', result)


num_1 = 5
num_2 = 0

find_number(numbers)
test(num_1, num_2)
