import itertools

colors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
for j in itertools.product(colors, repeat=4):
    i += 1
    print(j)
print('Колличество комбинаций: ', i)
