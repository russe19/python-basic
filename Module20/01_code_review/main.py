students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interes(dict):
    intereses = []
    for index in dict.values():
        intereses.extend(index['interests'])
    intereses = set(intereses)
    return intereses


def number_symbol(dict):
    symbols_second_name = ''
    number = 0
    for index in dict.values():
        symbols_second_name += index['surname']
    return len(symbols_second_name)


def ID_age(dict):
    pairs = []
    for i in dict:
        pairs.append((i, dict[i]['age']))
    return pairs


ID = ID_age(students)
intereses = interes(students)
len_sec_name = number_symbol(students)
print('Список пар "ID студента — возраст": ', ID)
print('Полный список интересов всех студентов: ', intereses)
print('Общая длина всех фамилий студентов: ', len_sec_name)
