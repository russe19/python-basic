import os
import types

tree = os.walk(os.path.abspath(os.path.join('..', '..')))
file = 'karma.log'


def path_gen(tree, file):
    for dirpath, dirnames, filenames in tree:
        s = os.path.split(dirpath)
        print(dirpath)
        for i_elem in filenames:
            if i_elem == file:
                s = 1
                yield os.path.abspath(os.path.join(dirpath, i_elem)), False
            yield os.path.abspath(os.path.join(dirpath, i_elem)), True


for i_elem, i_bool in path_gen(tree, file):
    if i_bool:
        print(i_elem)
    else:
        print('Файл найден! Путь к файлу:\n', i_elem)
        break
