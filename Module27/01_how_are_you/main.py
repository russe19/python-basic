from typing import Callable

def how_are_you(func: Callable) -> Callable:
    def nested_function() -> Callable:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        my_func = func()
        return func
    return nested_function

@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


test()