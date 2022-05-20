import os
import types

tree = os.walk(os.path.abspath(os.path.join('..', '..')))
print(tree)

path = os.path.abspath(os.path.join('..', '..', '..', '..', 'pythonProject1'))
file = 'linkedlist.PNG'

for dirpath, dirnames, filenames in tree:
    s = os.path.split(dirpath)
    print(dirpath)
    for i_elem in filenames:
        print(os.path.abspath(os.path.join(dirpath, i_elem)))
        if i_elem == file:
            print('Файл найден!\nПуть к файлу: ', os.path.abspath(os.path.join(dirpath, file)))
            break
