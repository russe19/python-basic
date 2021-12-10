films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_films = []
while True:
    film = input('Введите фильм: ')
    if film == 'end':
        break
    for index in range(len(films)):
        if film == films[index]:
            favorite_films.append(film)
        else:
            continue
print(favorite_films)