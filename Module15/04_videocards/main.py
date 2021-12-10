graphics_cards = []
new_graphics_cards = []
number = int(input('Кол-во видеокарт: '))
old = 0
for index in range(number):
    print(index + 1, 'Видеокарта: ', end='')
    card = int(input())
    if card > old:
        old = card
    graphics_cards.append(card)
print('Старый список видеокарт: ', graphics_cards)
for i in range(number):
    if graphics_cards[i] != old:
        new_graphics_cards.append(graphics_cards[i])
print('Новый список видеокарт: ', new_graphics_cards)

