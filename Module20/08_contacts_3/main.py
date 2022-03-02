contacts = {}
keys = []
values = []
new_key = []
new_keys = ''

while True:
    print('Введите номер действия:  \n1. Добавить контакт \n2. Найти человека ')
    act = int(input())

    if act == 1:
        name = input('Введите имя и фамилию нового контакта (через пробел): ')
        name = tuple(name.split())
        number = int(input('Введите номер телефона: '))
        contacts[name] = number
        print(contacts)

    elif act == 2:
        second_name = input('Введите фамилию для поиска: ')

        for key in contacts.keys():
            keys.append(key)

        for value in contacts.values():
            values.append(value)

        for index in range(len(keys)):
            if second_name in keys[index]:
                new_key = list(keys[index])
                new_keys = ' '.join(new_key)
                print(new_keys, values[index])