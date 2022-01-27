text = 'aaAAbbсaaaA'
print('Введите строку: ', text)
s = [i for i in text]
ss = []
summ = 1
print('\n\nЗакодированная строка: ', end='')
for i in range(len(text) - 1):
    if text[i] != text[i + 1]:
        print(text[i] + str(summ), end='')
        summ = 1
    else:
        summ += 1
if text[len(text) - 1] != text[len(text) - 2]:
    print(text[len(text) - 1] + str(summ))
else:
    summ += 1