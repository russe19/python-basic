text = input('Введите текст: ')
text_dict = {}
for i in text:
    if i in text_dict:
        text_dict[i] += 1
    else:
        text_dict[i] = 1

new = {}
for j in range(1,4):
    new[j] = []
for index in text_dict:
    if text_dict[index] == 1:
        new[1].append(index)
    if text_dict[index] == 2:
        new[2].append(index)
    if text_dict[index] == 3:
        new[3].append(index)
print(new)
