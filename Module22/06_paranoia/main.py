alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
order = 0

file = open('text.txt', 'r', encoding='utf-8')
data = file.read()
data = data.split('\n')
file.close()

file_2 = open('cipher_text.txt', 'w', encoding='utf-8')

for i_str in data:
    order += 1
    for i_sym in i_str:
        str = ''
        if i_sym in alphabet_lower:
            index = alphabet_lower.index(i_sym)
            if i_sym == alphabet_lower[index]:
                i_sym = alphabet_lower[(index + order) % len(alphabet_lower)]
                str += i_sym
            file_2.write(str)
        else:
            index = alphabet_upper.index(i_sym)
            if i_sym == alphabet_upper[index]:
                i_sym = alphabet_upper[(index + order) % len(alphabet_upper)]
                str += i_sym
            file_2.write(str)
    file_2.write('\n')
