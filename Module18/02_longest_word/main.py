text = input('Введите строку: ')
text_list = text.split()
numbers = [len(text_list[i]) for i in range(len(text_list))]
max_num = max(numbers)
number = numbers.index(max_num)
print('Самое длинное слово: ', text_list[number])
print('Длина этого слова: ', max_num)
