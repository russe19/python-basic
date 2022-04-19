def move(numbers, x, y):
    for disk in numbers:
        print('Переложить диск', disk, 'со стержня номер', x, 'на стержень номер', y)


num = int(input('Введите количество дисков: '))
numbers = []
for i in range(num + 1):
    numbers.append(i)
move(numbers[1:num], 1, 2)
move(numbers[num:num + 1], 1, 3)
move(numbers[num - 1:0:-1], 2, 3)
