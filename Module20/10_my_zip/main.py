new_str = input('Строка: ')
new_tuple = tuple(input('Кортеж чисел: ').split())
len_zip = min(len(new_str), len(new_tuple))
print('Вывод: ', )
for index in range(len_zip):
    print((new_str[index], new_tuple[index]))
