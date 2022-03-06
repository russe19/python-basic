count_contry = int(input('Количество стран: '))
num_list_contry = ['Первая', 'Вторая', 'Третья', 'Четвертая', 'Пятая', 'Шестая', 'Седьмая', 'Восьмая', 'Девятая', ]
num_list_city = ['Первый', 'Второй', 'Третий']
con = dict()

for i in range(count_contry):
    con[i] = dict()
    data = input('{0} страна: '.format(num_list_contry[i])).split(' ')
    con[i]['Страна'] = data[0]
    con[i]['Города'] = []
    for j in data[1:]:
        con[i]['Города'].append(j)

for j in range(3):
    city = input('\n{0} город: '.format(num_list_city[j]))
    flag = True
    for index_cont in range(count_contry):
        if city in con[index_cont]['Города']:
            print('Город', city, ' расположен в стране', con[index_cont]['Страна'], '.')
            flag = False
    if flag:
        print('По городу', city,' данных нет.')
