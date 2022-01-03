people_lst = []

people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', number, 'человек')

for i in range(1, people + 1):
    people_lst.append(i)

countdown = 0
while people > 1:
    print('\nТекущий круг людей: ', people_lst)
    if people == countdown:
        countdown = 0
    print('Начало счёта с номера ', people_lst[countdown])
    countdown = (number - 1 + countdown) % people
    print('Выбывает человек под номером ', people_lst[countdown])
    people_lst.remove(people_lst[countdown])
    people -= 1
print('\nОстался человек под номером ', people_lst[0])