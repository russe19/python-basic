def one_shift(list):
    s = 0
    t = len(list)
    s = list[t - 1]
    for i in range(len(list)):
        list[t - i - 1] = list[t - i - 2]
    list[0] = s
    return list

shift = int(input('Сдвиг: '))
amount = int(input('Введите колличество элементов: '))
list = []
initial_list = []

for i in range(amount):
    number = int(input('Введите элемент: '))
    list.append(number)

for i in range(len(list)):
    initial_list.append(list[i])

for _ in range(shift):
    list = one_shift(list)
print('\n\nСдвиг: ', shift)
print('Изначальный список: ', initial_list)
print('Сдвинутый список: ', list)