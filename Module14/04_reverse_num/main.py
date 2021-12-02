# TODO здесь писать код
number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите второе число: '))


def revers(number):
    count = 0
    x = number
    while x != 0:
        x //= 10
        count += 1
    x = 0
    s1 = 0
    for l in range(1, count + 1):
        s1 = number % 10
        x += s1 * (10 ** (count - l))
        number //= 10
    return x


def separation(number):
    count = 0
    while number % 1 != 0:
        number *= 10
        count += 1
        integer = number // 10 ** count
        fraction = number % 10 ** count
    integer_revers = revers(integer)
    fraction_revers = revers(fraction)
    fraction_revers /= 10 ** count
    return integer_revers, fraction_revers

number_1_integer, number_1_fraction = separation(number_1)
number_2_integer, number_2_fraction = separation(number_2)

new_num_1 = number_1_integer + number_1_fraction
print('Первое число наоборот: ', new_num_1)
new_num_2 = number_2_integer + number_2_fraction
print('Второе число наоборот: ', new_num_2)

print('Сумма: ', new_num_1 + new_num_2)


