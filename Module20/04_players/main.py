players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

new_players = []

for key, value in players.items():
    key_value = key + value
    new_players.append(key_value)
print('Вывод: ', new_players)
