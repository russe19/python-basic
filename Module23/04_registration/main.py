def val_exception(i_elem):
    try:
        new = i_elem.split()
        if len(new) != 3:
            raise IndexError
        if not new[0].isalpha():
            raise NameError
        if '@' not in new[1] or '.' not in new[1]:
            raise SyntaxError
        if int(new[2]) < 10 or int(new[2]) > 99:
            raise ValueError
    except IndexError:
        file_2.write(str(new) + '  НЕ присутствуют все три поля' + '\n')
        file_1.write(str(new) + '\n')
    except NameError:
        file_2.write(str(new) + '  Поле имени содержит НЕ только буквы' + '\n')
        file_1.write(str(new) + '\n')
    except SyntaxError:
        file_2.write(str(new) + '  Поле «Имейл» НЕ содержит @ и . (точку)' + '\n')
        file_1.write(str(new) + '\n')
    except ValueError:
        file_2.write(str(new) + '  Поле «Возраст» НЕ является числом от 10 до 99' + '\n')
        file_1.write(str(new) + '\n')


file = open('registrations.txt', 'r', encoding='utf-8')
file_1 = open('registrations_good.txt', 'w', encoding='utf-8')
file_2 = open('registrations_bad.txt', 'w', encoding='utf-8')

try:
    file_1.write('Содержимое файла registrations_good.log:' + '\n')
    file_2.write('Содержимое файла registrations_bad.log:' + '\n')
    for i_elem in file:
        val_exception(i_elem)
finally:
    file.close()
    file_1.close()
    file_2.close()
