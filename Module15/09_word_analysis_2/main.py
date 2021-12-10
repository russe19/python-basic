word = input('Введите слово: ')
word_list = list(word)
revers_word = []
number = len(word_list)
print(word_list[number - 1])

for i in range(number):
    num = word_list[number - 1 - i]
    revers_word.append(num)
print(revers_word)

if word_list == revers_word:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')