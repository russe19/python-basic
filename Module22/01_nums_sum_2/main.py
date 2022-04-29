import os

data_1 = open('numbers.txt', 'r', encoding='utf-8')
open_data = data_1.read()
data_1.close()
summ = 0
numbers = open_data.split()
data_2 = open('answer.txt', 'w')
for i_elem in numbers:
    summ += int(i_elem)
open_data_2 = data_2.write(str(summ))
data_2.close()
