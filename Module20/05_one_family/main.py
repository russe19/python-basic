def func_sec_name(name):
    name_second = ''
    if name[len(name) - 1] == 'а':
        for index in range(len(name) - 1):
            name_second += name[index]
    else:
        for symbol in name:
            name_second += symbol
        name_second += 'а'
    return name_second


people = {
    ("Сидоров", "Никита"): 35,
    ("Сидорова", "Алина"): 34,
    ("Сидоров", "Павел"): 10,
    ("Иванов", "Саша"): 34,
    ("Петрова", "Лена"): 10
}

names = []
ages = []
second_name = input('Введите фамилию: ')
for name, age in people.items():
    names.append(name)
    ages.append(age)
print('Возраст всех членов одной семьи: ', end='')

for i in range(len(names)):
    name_diff = func_sec_name(second_name)
    if name_diff in names[i] or second_name in names[i]:
        print(ages[i], ' ', end='')
