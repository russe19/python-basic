number = int(input('Сколько записей вносится в протокол? '))
players = {}
revers = {}
names = []
vals = []

for order in range(number):
    print(order + 1, 'запись: ', end='')
    data = input().split(' ')

    if data[1] in players:
        if int(data[0]) > players[data[1]]:
            players.pop(data[1])
            players[data[1]] = int(data[0])
    else:
        players[data[1]] = int(data[0])

for name, val in players.items():
    names.append(name)
    vals.append(val)

sort_value = sorted(players.values(), reverse=True)

for player_value in sort_value:
    for player_name in players:
        if players[player_name] == player_value:
            revers[player_name] = players[player_name]

place = 0

for new_player_name in revers:
    place += 1
    print(place, ' место. ', new_player_name, ' (', revers[new_player_name], ')', sep='', )
    if place == 3:
        break
