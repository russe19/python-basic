number = int(input('Введите количество заказов: '))
num_list = ['Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый', 'Шестой', 'Седьмой', 'Восьмой', 'Девятый', ]
data_list = []
for i in range(number):
    order = input('{0} заказ: '.format(num_list[i]))
    order_list = order.split()
    data_list.append(order_list)
print(data_list)

name_set = set()
for i in range(number):
    name_set.add(data_list[i][0])
sorted(name_set)
print(name_set)

for name in name_set:
    print(name)
    name_dict = {}
    for i in range(number):
        if name == data_list[i][0]:
            if data_list[i][1] in name_dict:
                name_dict[data_list[i][1]] += int(data_list[i][2])
            else:
                name_dict[data_list[i][1]] = int(data_list[i][2])
    sorted_list = sorted(name_dict)
    new_name_dict = {}
    for pizza in sorted_list:
        new_name_dict[pizza] = name_dict[pizza]
        print('  ', pizza, '-', new_name_dict[pizza])
