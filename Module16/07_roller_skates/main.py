def increase(num, lst):
    for i in range(num):
        for j in range(i,num):
            if lst[i] >= lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

skates_list = []
people_list = []

skates = int(input('Кол-во коньков: '))
for i in range(skates):
    print('Размер', i + 1, 'пары: ', end='')
    skate = int(input())
    skates_list.append(skate)

people = int(input('\nКол-во людей: '))
for i in range(people):
    print('Размер ноги', i + 1, 'человека: ', end='')
    person = int(input())
    people_list.append(person)

increase(skates, skates_list)
increase(people, people_list)

s = 0
for i in range(skates):
        if skates_list[i] >= min(people_list):
            s += 1
            people_list.remove(min(people_list))
print('Наибольшее кол-во людей, которые могут взять ролики: ', s)

# TODO в таком случае произошла ошибка:
# Кол-во коньков: 2
# Размер 1 пары: 12
# Размер 2 пары: 21
#
# Кол-во людей: 1
# Размер ноги 1 человека: 12
# TODO хотя правильный ответ должен был отобразиться: 1
