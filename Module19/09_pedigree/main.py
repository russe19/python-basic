number = int(input('Введите количество человек: '))
num_list = ['Первая', 'Вторая', 'Третья', 'Четвертая', 'Пятая', 'Шестая', 'Седьмая', 'Восьмая', 'Девятая', ]
names_dict = {}
s = []
for i in range(number - 1):
    names_dict[i] = input('{0} пара: '.format(num_list[i])).split()
dictionary = {}

for j in range(len(names_dict)):
    dictionary[names_dict[j][0]] = names_dict[j][1]
new_dict = {}
pre = set()
new_pre = set()

for value in dictionary.values():
    if value not in dictionary.keys():
        new_dict[value] = 0
        pre.add(value)
    else:
        new_dict[value] = 1

for key in dictionary.keys():
    new_dict[key] = 1


while len(pre) < number:
    for i in dictionary:
        if dictionary[i] in pre:
            new_pre.add(i)
        else:
            new_dict[i] += 1
    pre = pre | new_pre
    new_pre = set()

print()
for name_index in sorted(new_dict):
    print(name_index, new_dict[name_index])