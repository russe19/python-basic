def replacement(i, alphabet, shift):
    if i in alphabet:
        num = alphabet.index(i)
        b = len(alphabet)
        s = alphabet[(num + shift) % b]
    else:
        s = ' '
    return  s

st = ''
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
            'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',]
text = input('Введите сообщение: ')
text_list = list(text)
shift = int(input('Введите сдвиг: '))

new_text = [replacement(i, alphabet, shift) for i in text_list]
for i in new_text:
    st += i
print('Зашифрованное сообщение: ',st)