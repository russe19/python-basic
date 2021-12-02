number = int(input('Введите число: '))

for n in range(2, number + 1):
    if number % n != 0:
        continue
    else:
        break
print('Наименьший делитель, отличный от единицы: ', n)