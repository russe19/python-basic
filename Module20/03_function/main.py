tuple_and_number = ((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2)
numbers = []
flag = False

amount_of_numbers = tuple_and_number[0].count(tuple_and_number[1])

if amount_of_numbers == 0:
    numbers = []
elif amount_of_numbers == 1:
    ind = tuple_and_number[0].index(tuple_and_number[1])
    numbers = tuple_and_number[0][ind:]
else:
    for i in tuple_and_number[0]:
        if flag:
            numbers.append(tuple_and_number[0][i])
            if tuple_and_number[1] == tuple_and_number[0][i]:
                break
        if tuple_and_number[1] == tuple_and_number[0][i]:
            flag = True
            numbers.append(tuple_and_number[0][i])
new_numbers = tuple(numbers)
print('Вывод: ', new_numbers)
