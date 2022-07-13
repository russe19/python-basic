import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    """ Декоратор дает возможность другому декоратору принимать произвольные аргументы """

    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_to_enhance(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """ Декоратор """

    @functools.wraps(func)
    def wrapper(*func_args, **func_kawrgs) -> Callable:
        print('Переданные арги к кварги в декоратор:', dec_args, dec_kwargs)
        return func(*func_args, **func_kawrgs)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
