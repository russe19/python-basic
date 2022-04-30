file = open('registrations.txt', 'r', encoding='utf-8')
file_2 = open('registrations_good.txt', 'w', encoding='utf-8')
try:
    for i_elem in file:
        try:
            new = i_elem.split()
            if len(new) != 3:
                raise ValueError
            if not new[0].isalpha():
                raise NameError
            if '@' not in new[1] or '.' not in new[1]:
                raise SyntaxError
            if int(new[2]) < 10 or int(new[2]) > 99:
                raise Exception
        except ValueError:
            file_2.write(str(new) + '  Колличество элементов строки не равно трем' + '\n')
        except NameError:
            file_2.write(str(new) + '  Поле «Имя» содержит неподходящие символы' + '\n')
        except SyntaxError:
            file_2.write(str(new) + '  Поле «Имейл» НЕ содержит @ и . (точку)' + '\n')
        except Exception:
            file_2.write(str(new) + '  Поле «Возраст» НЕ является числом от 10 до 99' + '\n')
finally:
    file.close()
    file_2.close()
# TODO по условию задания требуется записывать ошибки в файл с другим названием:
#  `registrations_bad.log` — для ошибочных, записывать строку и вид ошибки.
#  в registrations_good.txt нужно записывать корректные строки
