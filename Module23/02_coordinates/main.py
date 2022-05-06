import random


def f(x, y):
    try:
        x += random.randint(0, 10)
        y += random.randint(0, 5)
        if y == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        return print('Деление на ноль в первой функции')
    return x / y


def f2(x, y):
    try:
        x -= random.randint(0, 10)
        y -= random.randint(0, 5)
        if x == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        return print('Деление на ноль во второй функции')
    return y / x


try:
    file = open('coordinates.txt', 'r')
    file_2 = open('result.txt', 'w')
    for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        res2 = f2(int(nums_list[0]), int(nums_list[1]))
        try:
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            print(str(my_list))
            file_2.write(''.join(str(my_list)) + '\n')
        except Exception:
            print("Что-то пошло не так при сортировке")
except Exception:
    print("Что-то пошло не так")
finally:
    file.close()
    file_2.close()
