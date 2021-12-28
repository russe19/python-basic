violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

number = int(input('Сколько песен выбрать? '))

summ = 0
for i in range(number):
    print('Название', i + 1, ' песни:', end=' ')
    name = input()
    for index in range(len(violator_songs)):
        if name == violator_songs[index][0]:
            summ += violator_songs[index][1]
print('Общее время звучания песен: ', round(summ, 2), ' минут')