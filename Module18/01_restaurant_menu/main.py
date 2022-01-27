dishes = 'утиное филе;фланк-стейк;банановый пирог;плов'
print('Доступное меню: ', dishes)
dishes_list = dishes.split(';')
new_dishes = (', ').join(dishes_list)
print('\n\nНа данный момент в меню есть:', new_dishes)