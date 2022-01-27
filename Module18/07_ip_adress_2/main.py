address = input('Введите IP: ')
address_list = address.split('.')

flag = True
while True:
    if len(address_list) != 4:
        flag = False
        print('Адрес — это четыре числа, разделённые точками.')
    if flag is False:
        break
    for i in range(len(address_list)):
        if address_list[i].isdigit() == False:
            flag = False
            print(address_list[i], ' — это не целое число.')
            break
    if flag is False:
        break
    for i in range(len(address_list)):
        if int(address_list[i]) > 255:
            flag = False
            print(address_list[i], 'превышает 255.')
            break
    if flag is False:
        break
    print('IP-адрес корректен.')
    break