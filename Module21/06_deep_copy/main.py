def site_func(name):
    site = {
        'html': {
            'head': {
                'title': 'Куплю/продам {} недорого'.format(name)
            },
            'body': {
                'h2': 'У нас самая низкая цена на {}'.format(name),
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }
    return site


full_list = list()
count = int(input('Сколько сайтов: '))
for _ in range(count):
    name = input('Введите название продукта для нового сайта: ')
    full_list.append(name)
    for name_in_list in full_list:
        print('\nСайт для', name_in_list, ':\nsite =', site_func(name_in_list))
