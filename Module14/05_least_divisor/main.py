# TODO здесь писать код
number = int(input('Введите число: '))

for n in range(2, number + 1):
    # TODO разверните условие и -2 строки
    if number % n != 0:
        continue
    else:
        break
print('Наименьший делитель, отличный от единицы: ', n)
