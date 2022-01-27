def shift(str):
    s = [str[(i + 1) % len(str)] for i in range(len(str))]
    return s


first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')

first_list = [i for i in first_str]
second_list = [i for i in second_str]

flag = True
if len(first_list) != len(second_list):
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    for i in range(len(first_list)):
        new_second = ''.join(second_list)
        second_list = shift(second_list)
        if new_second == first_str:
            flag = False
            print('\nПервая строка получается из второй со сдвигом', i, '.')
    if flag:
        print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
