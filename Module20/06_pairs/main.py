original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
first = []
second = []

for i in range(len(original_list)):
    if i % 2 == 0:
        first.append(i)
    else:
        second.append(i)

new = list(zip(first, second))
print('Вывод: ', new)
