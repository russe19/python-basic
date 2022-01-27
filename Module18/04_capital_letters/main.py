text = input('Введите строку: ')
text = text.lower()
text_list = text.split()
new_list = []

for i in range(len(text_list)):
    word = text_list[i]
    for index in range(len(word)):
        if index == 0:
            new_word = word[0].upper()
        else:
            new_word += word[index]
    new_list.append(new_word)
new_text = (' ').join(new_list)
print('\n\nРезультат:', new_text)