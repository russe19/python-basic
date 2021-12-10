word = input('Введите слово: ')
letters = []
check_letters = []
s = 0
for index in range(len(word)):
    if word[index] not in letters and word[index] not in check_letters:
        s += 1
        letters.append(word[index])
    elif word[index] in letters and word[index] not in check_letters:
        s -= 1
        check_letters.append(word[index])
print('Кол-во уникальных букв: ', s)