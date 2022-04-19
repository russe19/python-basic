# def sum_func_set(*args):
#     summ = 0
#     for i in args:
#         summ += i
#     return summ

def sum_func(data):
    summ = 0
    for elem in data:
        if isinstance(elem, int):
            summ += elem
        elif isinstance(elem, list):
            summ += sum_func(elem)
    return summ


data_set = 1, 2, 3, 4, 5
data_list = [[1, 2, [3]], [1], 3]

data_answer = sum_func(data_list)
# data_1 = sum_func(data_set)
print('Ответ в консоли: ', data_answer)
