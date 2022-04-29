def my_zip(data_1, data_2):
    if len(data_1) != 0 and len(data_2) != 0:
        total.append((data_1[0], data_2[0]))
        data_1 = data_1[1:]
        data_2 = data_2[1:]
        my_zip(data_1, data_2)
    return total


total = list()
data_1 = [4, 653, 7]
data_2 = 'dtgh'
my_zip(data_1, data_2)
for index in total:
    print(index)
