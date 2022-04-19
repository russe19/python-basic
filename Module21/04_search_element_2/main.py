site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key_y(my_key, depth, struct, my_depth):
    my_depth += 1
    if my_depth <= depth:
        if my_key in struct:
            return struct[my_key]
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key_y(my_key, depth, sub_struct, my_depth)
                if result:
                    break
        else:
            result = None
        return result


def find_key_n(my_key, struct):
    if my_key in struct:
        return struct[my_key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(my_key, sub_struct)
            if result:
                break
    else:
        result = None
    return result


my_key = input('Введите искомый ключ: ')
depth_selection = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if depth_selection == 'y':
    depth = int(input('Введите максимальную глубину: '))
    my_depth = 0
    value = find_key_y(my_key, depth, site, my_depth)
    if value:
        print(value)
    else:
        print('Такого ключа в структуре сайта нет.')
elif depth_selection == 'n':
    value = find_key_n(my_key, site)
    if value:
        print(value)
    else:
        print('Такого ключа в структуре сайта нет.')
else:
    print('Неверный ввод')
