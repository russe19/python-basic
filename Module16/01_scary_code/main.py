basic_list = [1, 5, 3]
first_list = [1, 5, 1, 5]
second_list = [1, 3, 1, 5, 3, 3]

basic_list.extend(first_list)

number_five = basic_list.count(5)
for _ in range(number_five):
    basic_list.remove(5)

basic_list.extend(second_list)

number_three = basic_list.count(3)

print('Кол-во цифр 5 при первом объединении:', number_five)
print('Кол-во цифр 3 при втором объединении:', number_three)
print('Итоговый список: ', basic_list)

