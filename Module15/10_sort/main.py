amount = int(input('Введите количество элементов: '))
number_list = []
for _ in range(amount):
    num = int(input('Введите число: '))
    number_list.append(num)

value = 0

for _ in range(amount):
    for i in range(amount - 1):
        if number_list[i] > number_list[i + 1]:
            value = number_list[i]
            number_list[i] = number_list[i + 1]
            number_list[i + 1] = value

print(number_list)
