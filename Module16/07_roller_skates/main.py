skates_list = []
people_list = []

skates = int(input('Кол-во коньков: '))
for index_skate in range(skates):
    print('Размер', index_skate + 1, 'пары: ', end='')
    skate = int(input())
    skates_list.append(skate)

people = int(input('\nКол-во людей: '))
for index_people in range(people):
    print('Размер ноги', index_people + 1, 'человека: ', end='')
    person = int(input())
    people_list.append(person)

summ = 0
while skates_list != []:
    if min(people_list) <= min(skates_list):
        summ += 1
        people_list.remove(min(people_list))
        skates_list.remove(min(skates_list))
    else:
        skates_list.remove(min(skates_list))
print('\nНаибольшее кол-во людей, которые могут взять ролики: ', summ)