import time
from typing import Callable


def timer(func: Callable) -> Callable:
    def nested_function() -> Callable:
        while True:
            first_time = time.time()
            dif = 0
            while dif < 2:
                second_time = time.time()
                dif = second_time - first_time
            my_func = func()
        return func

    return nested_function


@timer
def test() -> None:
    print('Проверка выполнена')


test()
