def couting(i_elem):
    if i_elem.endswith('\n'):
        i_elem = i_elem[:-1:]
    i_elements = i_elem.split(' ')
    if len(i_elements) != 3:
        count = None
    if i_elements[1] == '+':
        count = int(i_elements[0]) + int(i_elements[2])
    elif i_elements[1] == '-':
        count = (int(i_elements[0]) - int(i_elements[2]))
    elif i_elements[1] == '*':
        count = (int(i_elements[0]) * int(i_elements[2]))
    elif i_elements[1] == '/':
        count = (int(i_elements[0]) / int(i_elements[2]))  # TODO нужно предусмотреть возможность ошибки деления на 0
        # TODO ZeroDivisionError: division by zero
    else:
        count = None
    return count, i_elem


file = open('calc.txt', 'r')
summ = 0
str_count = 0
try:
    for i_elem in file:
        str_count += 1
        try:
            count, i_elem = couting(i_elem)
            if count == None:
                raise ValueError
            summ += count
        except ValueError:
            try:
                print('Обнаружена ошибка в строке: {} Хотите исправить?'.format(i_elem), end='')
                answer = input().lower()
                if answer == 'да':
                    try:
                        i_elem = input('Введите исправленную строку: ')
                        count, i_elem = couting(i_elem)
                        summ += count
                    except Exception:
                        print('В исправленной строке введены неверные данные!')
                elif answer == 'нет':
                    continue
                else:
                    raise SyntaxError
            except SyntaxError:
                print('Данные введены неверно!')
finally:
    print('Сумма результатов: ', summ)
    file.close()