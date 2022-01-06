text = input('Введите текст: ')
vowels = [x for x in text if x == 'a' or x == 'я' or x == 'о' or x == 'ё'
        or x == 'у' or x == 'ю' or x == 'э' or x == 'е' or x == 'ы' or x == 'и']

print('Список гласных букв: ', vowels)
print('Длина списка: ', len(vowels))