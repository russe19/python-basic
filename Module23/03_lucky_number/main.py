import random

change = 0
summ = 0
file = open('out_file.txt', 'w')
try:
    while summ < 777:
        try:
            change = random.randint(1, 13)
            num = int(input('Введите число: '))
            if change == 1:
                raise ValueError
            summ += num
            file.write(str(num) + '\n')
        except ValueError:
            print('Вас постигла неудача!')
            break
finally:
    file.close()
    print(file.closed)
