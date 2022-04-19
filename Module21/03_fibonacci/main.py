def febonachi(num_pos, pos, number, first_number, second_number):
    if num_pos != pos:
        pos += 1
        if pos % 2 == 0:
            first_number = number
        else:
            second_number = number
        number = first_number + second_number
        return febonachi(num_pos, pos, number, first_number, second_number)
    else:
        return number


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
pos = 1
number = 1
first_number = 0
second_number = 0
print('Число:', febonachi(num_pos, pos, number, first_number, second_number))
