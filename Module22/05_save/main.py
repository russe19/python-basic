import os


def path_func(path_elems):
    if len(path_elems) >= 2:
        new = os.path.join(path_elems[0], path_elems[1])
        path_elems[1] = new
        path_elems.remove(path_elems[0])
        path_func(path_elems)
    return path_elems[0]


s = ''
text = input('Введите строку: ')
# text = 'dfhgdf214214g'
path_elems = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split(' ')
# path_elems = ['Users', 'russe', 'PycharmProjects', 'Python_Basic2', 'Module22', '05_save']
path = path_func(path_elems)
name = input('Введите имя файла: ')
# name = 'answer1342'
name += '.txt'

print(os.path.abspath(os.path.join(os.path.sep, path, name)))
if os.path.exists(os.path.abspath(os.path.join(os.path.sep, path, name))):
    file = open(name, 'w', encoding='utf-8')
    answer = input('Вы действительно хотите перезаписать файл? (нет/да)')
    if answer == 'да':
        file.write(text)
        print('Файл успешно перезаписан!')
    elif answer == 'нет':
        print('Отмена запроса!')
    else:
        print('Ошибка ввода')
else:
    file = open(name, 'w', encoding='utf-8')
    file.write(text)
    print('Файл успешно перезаписан!')
file.close()

file = open(name, 'r', encoding='utf-8')
data = file.read()
print('Содержимое файла:\n', data)
file.close()
