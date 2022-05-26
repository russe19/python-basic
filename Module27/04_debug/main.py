from typing import Callable


def debug(func: Callable) -> Callable:
    def inner_function(*args, **kwargs) -> None:
        if func(*args, **kwargs)[2]:
            print(f"Вызывается {func.__name__}(name='{func(*args, **kwargs)[1]}', age={func(*args, **kwargs)[2]})")
        else:
            print(f"Вызывается {func.__name__}(name='{func(*args, **kwargs)[1]}')")
        print('{} вернула значение {}'.format(repr(func.__name__), repr(func(*args, **kwargs))))
        print(func(*args, **kwargs)[0])
        print()

    return inner_function


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age), name, age
    else:
        return "Привет, {name}!".format(name=name), name, age


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
