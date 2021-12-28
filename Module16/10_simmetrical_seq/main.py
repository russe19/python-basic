sequence = []
revers = []

num = int(input('Кол-во чисел: '))
for i in range(num):
    number = int(input('Число: '))
    sequence.append(number)

print('\nПоследовательность: ', end='')
for i in range(num):
    print(sequence[i], end=' ')

for i in range(len(sequence)):
    if sequence[i:] == sequence[i:][::-1]:
        print('\nНужно приписать чисел: ', i)
        break
print('Сами числа:', end=' ')
for index in sequence[:i][::-1]:
    print(index, end=' ')