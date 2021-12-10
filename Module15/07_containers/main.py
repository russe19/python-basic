number = int(input('Кол-во контейнеров: '))
flag = True
list_container = []
for i in range(number):
    container = int(input('Введите вес контейнера: '))
    if 0 >= container or container >= 200:
        print('Ошибка ввода')
        flag = False
        break
    else:
        list_container.append(container)
        continue
new_container = int(input('Введите вес нового контейнера: '))
index = 0
while new_container < list_container[index]:
    index += 1
list_container.insert(index, new_container)
print('Номер, куда встанет новый контейнер: ', index + 1)