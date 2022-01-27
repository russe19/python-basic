def capital_letters(pass_list):
    s = False
    for i in pass_list:
        if i.isupper():
            s = True
    return s

def lower_case(pass_list):
    s = False
    for i in pass_list:
        if i.islower():
            s = True
    return s

def numbers(pass_list):
    s = False
    for i in pass_list:
        if i.isdigit():
            s = True
    return s

while True:
    password = input('Придумайте пароль: ')
    pass_list = [i for i in password]
    if capital_letters(pass_list) and lower_case(pass_list) and numbers(pass_list) and len(pass_list) > 7:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')

# TODO оформить код по правилам PEP8 (для этого существует сочетание клавиш, доступное в PyCharm)
