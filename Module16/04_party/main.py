guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек: ', guests)
    command = input('Гость пришёл или ушёл? ')
    if command == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            guests.append(name)
            print('Привет, Алекс!')
        else:
            print('Прости,', name, ', но мест нет.')
    if command == 'ушёл':
        name = input('Имя гостя: ')
        if name in guests:
            guests.remove(name)
            print('Пока,', name, '!')
        else:
            print('Такого гостя нет!')
    if command == 'Пора спать':
        break
print('Вечеринка закончилась, все легли спать.')