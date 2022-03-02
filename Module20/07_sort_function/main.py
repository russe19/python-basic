original = (6, 3, -1, 8, 4, 10, -5)
flag = True

for i in original:
    if i % 1 != 0:
        flag = False

if flag:
    new = tuple(sorted(original))
    print('Вывод: ', new)
else:
    print('Вывод: ', original)