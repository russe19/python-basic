names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
names_first_day = []
for index in range(len(names)):
    if index % 2 == 0:
        names_first_day.append(names[index])
print(names_first_day)

