import itertools

colors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in itertools.combinations_with_replacement(colors, 4):
    print(i)
