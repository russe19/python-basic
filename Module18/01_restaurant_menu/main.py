dishes = 'утиное филе;фланк-стейк;банановый пирог;плов'
print('Доступное меню: ', dishes)
dishes_list = dishes.split(';')
new_dishes = ', '.join(dishes_list)  # NOTE доп. круглые скобки здесь не нужны были
print('\n\nНа данный момент в меню есть:', new_dishes)
