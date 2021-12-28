friends = []

number = int(input('Кол-во друзей: '))
receipts = int(input('Долговых расписок: '))

for index in range(1, number + 1):
    friends.append(0)

for i in range(receipts):
    print(i + 1, 'расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    money = int(input('Сколько: '))
    friends[to_whom - 1] -= money
    friends[from_whom - 1] += money

print('Баланс друзей: ')
for i in range(number):
    print(i + 1, ':', friends[i])