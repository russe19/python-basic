num = int(input('Введите колличество пар слов: '))
num_list = ['Первая', 'Вторая', 'Третья', 'Четвертая', 'Пятая', 'Шестая', 'Седьмая', 'Восьмая', 'Девятая', ]
s = {}
for i in range(num):
    s[i] = input('{0} пара: '.format(num_list[i]))
    s[i] = s[i].lower()
sum = []
for j in range(num):
    double = s[j].split(' - ')
    sum.append(double)
while True:
    word = input('Введите слово: ')
    word = word.lower()
    flag = True
    for index in range(num):
        if word == sum[index][0]:
            print('Синоним:', sum[index][1].title())
            flag = False
        elif word == sum[index][1]:
            print('Синоним:', sum[index][0].title())
            flag = False
    if flag:
        print('Такого слова в словаре нет.')