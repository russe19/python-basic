import random

number = int(input('Введите максимальное число: '))
hidden_number = random.randint(1, number)

correct_numbers = set()
incorrect_numbers = set()
text = ''
while text != 'Помогите!':
    text = input('Нужное число есть среди вот этих чисел: ')
    text_list = text.split()
    if str(hidden_number) in text_list:
        print('Ответ Артёма: Да')
        for i in text_list:
            if i not in incorrect_numbers and i not in correct_numbers:
                correct_numbers.add(i)
        text_set = set(text_list)
        correct_numbers = correct_numbers & text_set
    elif str(hidden_number) not in text_list:
        print('Ответ Артёма: Нет')
        for i in text_list:
            incorrect_numbers.add(i)
            if i in correct_numbers:
                correct_numbers.remove(i)
    else:
        break
correct_numbers = sorted(correct_numbers)
print('Артём мог загадать следующие числа:', end=' ')
for i in correct_numbers:
    print(i, end=' ')


