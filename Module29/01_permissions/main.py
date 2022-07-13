import functools
from builtins import PermissionError
from collections.abc import Callable


def check_permission(_func=None, *, name: str = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Callable:
            try:
                if name in user_permissions:
                    func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError as ex:
                print('{}: У пользователя недостаточно прав, чтобы выполнить функцию {}'.format(type(ex).__name__,
                                                                                                func.__name__))
            return func

        return wrapped

    if _func is None:
        return decorator
    return decorator(_func)


user_permissions = ['admin']


@check_permission(name='admin')
def delete_site():
    print('Удаляем сайт')


@check_permission(name='user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
