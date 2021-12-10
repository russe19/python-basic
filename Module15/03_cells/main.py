efficiency = [3, 0, 6, 2, 10]
rang = [1, 2, 3, 4, 5]
number = int(input('Кол-во клеток: '))
for index in range(number):
    print('Эффективность', rang[index], 'клетки: ', efficiency[index])
print('\n\nНеподходящие значения:', end=' ')
for index in range(number):
    if efficiency[index] < rang[index]:
        print(efficiency[index], end=' ')
