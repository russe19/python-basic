import os

data = open('zen.txt', 'r', encoding='utf-8')
open_data = data.read()
data_st = open_data.split('\n')
for i_elem in data_st[::-1]:
    print(i_elem)
data.close()
