import itertools

colors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
for _ in itertools.combinations_with_replacement(colors, 4):
    i += 1
print(i)  # 715
# TODO Всего вариантов должно быть 10 000 (математика: 10*10*10*10)
#  сейчас выдаёт не всё, которые ожидаем потому, что здесь нужен другой метод или подход
