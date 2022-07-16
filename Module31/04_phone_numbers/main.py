import re
from typing import Callable

list_of_numbers = ['9999999999', '999999-999', '99999x9999']

count = 0


def func(elem):
    global count
    count += 1
    s = re.search(r'[89]\d{9}', elem)
    if s == None:
        return '{} номер: не подходит'.format(count)
    else:
        return '{} номер: всё в порядке'.format(count)


new = map(lambda elem: func(elem), list_of_numbers)
for i in new:
    print(i)
