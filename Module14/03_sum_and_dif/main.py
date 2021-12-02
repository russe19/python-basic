number = int(input('Введите число: '))

def summ(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def amount(x):
    s = 0
    while x > 0:
        x //= 10
        s += 1
    return s

print('Сумма цифр: ', summ(number))

print('Кол-во цифр в числе: ', amount(number))

print('Разность суммы и кол-ва цифр: ', summ(number) - amount(number))
