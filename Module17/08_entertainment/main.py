import random

sticks_str = ''
sticks = int(input('Кол-во палок: '))
sticks_list = ['|' for _ in range(sticks)]
throw = int(input('Кол-во бросков: '))
for i in range(throw):
    num_1 = random.randint(1, sticks)
    num_2 = random.randint(1, sticks)
    if num_1 > num_2:
        print('Бросок', i + 1, '. Сбиты палки с номера', num_2, '\nпо номер', num_1)
        for index in range(num_2 - 1, num_1):
            sticks_list[index] = '.'
    else:
        print('Бросок', i + 1, '. Сбиты палки с номера', num_1, '\nпо номер', num_2)
        for index in range(num_1 - 1, num_2):
            sticks_list[index] = '.'
for i in sticks_list:
    sticks_str += i
print('Результат: ', sticks_str)