from collections.abc import Callable
import functools
from datetime import datetime
import time
import re
import math


def decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        time_now = re.split("-| |:", str(datetime.now()))
        Y, b, d, H, M, S = time_now
        S = str(math.floor(float(S)))
        text = "b d Y - H:M:S"
        if text == "b d Y - H:M:S":
            time_now = '{} {} {} - {}:{}:{}'.format(b, d, Y, H, M, S)
        start = time.time()
        print('\tЗапускается {}. Дата и время запуска: {}'.format(func.__qualname__, time_now))
        decor = func(*args, **kwargs)
        stop = time.time()
        print('\tЗавершение {}, время работы = {}'.format(func.__qualname__, round(stop - start, 3)))
        return func

    return wrapped


def log_methods(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for i in dir(cls):
            if i.startswith('__') is False:
                cur_meth = getattr(cls, i)
                decorated_method = decorator(cur_meth)
                setattr(cls, i, decorated_method)
        return cls

    return decorate


@log_methods(decorator)
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods(decorator)
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
