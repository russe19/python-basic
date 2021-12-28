first_list = []
second_list = []

for i in range(3):
    num = int(input('Введите число: '))
    first_list.append(num)

for i in range(7):
    num = int(input('Введите число: '))
    second_list.append(num)

print('Первый список: ', first_list)
print('Второй список: ', second_list)

first_list.extend(second_list)
second_list = []
for i in first_list:
    while first_list.count(i) != 1:
        first_list.remove(i)
print('Новый первый список с уникальными элементами: ', first_list)