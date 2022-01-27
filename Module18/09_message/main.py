alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_list = [i for i in alphabet]
up_alphabet_list = [i.upper() for i in alphabet]
alphabet_list.extend(up_alphabet_list)

message = input('Сообщение: ')
message_list = [i  for i in message]

message_list = [i  for i in message ]
new_list = []
new_new = ''
s = []
for i in range(len(message_list)):
    if message_list[i] in alphabet_list and i == (len(message_list) - 1):
        new_new += message_list[i]
        new_list.append(new_new)
    elif message_list[i] in alphabet_list:
        new_new += message_list[i]
    else:
        if message_list[i - 1] in alphabet:
            new_list.append(new_new)
            new_list.extend(message_list[i])
            new_new = ''
        else:
            new_list.extend(message_list[i])
            new_new = ''

new = []
for sym in new_list:
    sym = sym[::-1]
    new.append(sym)
new_str = ''.join(new)
print('\nНовое сообщение: ', new_str)

# TODO оформить код по правилам PEP8
