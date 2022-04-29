data = open('zen.txt', 'r')
open_data = data.read().lower()
st = open_data.split()
letters = []
symbols = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
rare_letters = dict()

for i_letter in open_data:
    if i_letter in alphabet:
        letters.append(i_letter)

print('Количество букв в файле: ', len(letters))

for i_sym in open_data:
    if i_sym in alphabet or i_sym == ' ':
        symbols += i_sym
words = symbols.split(' ')

print('Количество слов в файле: ', len(words))

str = open_data.split('\n')
print('Количество строк в файле:', len(str))

for i_rare_letter in letters:
    if i_rare_letter in rare_letters:
        rare_letters[i_rare_letter] += 1
    else:
        rare_letters[i_rare_letter] = 1

for i_let in rare_letters:
    if rare_letters[i_let] == min(rare_letters.values()):
        print('Наиболее редкая буква: ', i_let)
