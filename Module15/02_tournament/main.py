names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
names_first_day = []
for index in range(1, 8, 2):
    names_first_day.append(names[index])
print(names_first_day)

# TODO чётные индексы определены неверно
# TODO правильный ответ должен получиться такой:
#  ['Артемий', 'Влад', 'Дима', 'Женя']
