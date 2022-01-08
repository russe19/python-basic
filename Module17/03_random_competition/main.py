import random

first_squad = [random.randint(500, 1000) / 100 for _ in range(20)]
second_squad = [random.randint(500, 1000) / 100 for _ in range(20)]
third_squad = [first_squad[i] if first_squad[i] > second_squad[i] else second_squad[i] for i in range(20)]
print('Первая команда: ', first_squad)
print('Вторая команда: ', second_squad)
print('Победители тура: ', third_squad)

# зачёт!
