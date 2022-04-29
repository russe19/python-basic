user_name = input('Введите имя пользователя: ')
while True:
    print('Чтобы увидеть текст чата введите 1, чтобы написать сообщение введите 2')
    response = input('Введите 1 или 2: ')
    if response == '1':
        try:
            with open('chat.txt', 'r') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Служебное сообщение: ничего нет\n')
    elif response == '2':
        new_message = input('Введите сообщение: ')
        with open('chat.txt', 'a') as file:
            file.write('{name}:{message}\n'.format(name=user_name, message=new_message))
    else:
        print('Неизвестная коменда\n')
