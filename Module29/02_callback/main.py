import functools
from collections.abc import Callable

app = {}


def callback(_func: Callable = None, key: str = None, app: dict = None) -> Callable:
    def calll(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            app[key] = func
            return func

        return wrapped

    if _func is None:
        return calll
    return calll(_func)


@callback(key='//', app=app)
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


example()

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
