name = input('Название файла: ')
if name.startswith('@') or name.startswith('№') or name.startswith('$') or name.startswith('%') \
        or name.startswith('^') or name.startswith('&') or name.startswith('*') or name.startswith('()'):
    print('Ошибка: название начинается на один из специальных символов.')
elif name.endswith('.txt') or name.endswith('.docx'):
    print('Файл назван верно.')
else:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
