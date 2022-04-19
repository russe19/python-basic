def is_prime(indexs, symbols):
    numbers = []
    new_symbols = []
    for index in indexs:
        flag = False
        for j in range(2, index):
            if index % j == 0:
                flag = True
        if flag == False and index >= 2:
            numbers.append(index)
            new_symbols.append(symbols[index])
    return new_symbols


# input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input = 'О Дивный Новый мир!'
input = [i for i in input]
new_index = []
new_symbol = []
for index, symbol in enumerate(input):
    new_symbol.append(symbol)
    new_index.append(index)
print('Вывод: ', is_prime(new_index, new_symbol))
