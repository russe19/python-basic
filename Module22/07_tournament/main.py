file = open('first_tour.txt', 'r', encoding='utf-8')
data = file.read().split()
grade = data[0]

data.remove(grade)

person = dict()
account = 0

for i in range(len(data) // 3):
    name = data[i * 3 + 1][0] + '.' + data[i * 3]
    person[name] = data[i * 3 + 2]

sort_values = sorted(person.values())[::-1]

file = open('second_tour.txt', 'w', encoding='utf-8')

while sort_values[0] > grade:
    account += 1
    conclusion = ''
    for key, value in person.items():
        if sort_values[0] == value:
            conclusion = str(i + 1) + ') ' + str(key) + ' ' + str(value)
            file.write(str(account) + ') ' + str(key) + ' ' + str(value) + '\n')
    sort_values.remove(sort_values[0])
