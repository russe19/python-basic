file = open('people.txt', 'r', encoding='utf-8')
summ = 0
count = 0
for i_word in file:
    try:
        count += 1
        length = len(i_word)
        if i_word.endswith('\n'):
            length -= 1
        summ += length
        if length < 4:
            raise ValueError
    except ValueError:
        print('Ошибка: менее трёх символов в строке {} .'.format(count))

print('Общее количество символов: ', summ)