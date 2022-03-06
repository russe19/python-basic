violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

num_list = ['первой', 'второй', 'третьей', 'четвертой', 'пятой', 'шестой', 'седьмой', 'восьмой', 'девятой', ]
time = 0
songs = int(input('Сколько песен выбрать? '))
for i in range(songs):
    song = input('Введите {0} песни: '.format(num_list[i]))
    if song in violator_songs:
        time += violator_songs[song]
print('Общее время звучания песен: ', time, 'минуты')