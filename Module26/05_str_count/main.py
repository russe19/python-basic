import os

tree = os.walk(os.path.abspath(os.path.join('..')))
print(tree)

summ = 0
for dirpath, dirnames, filenames in tree:
    s = os.path.split(dirpath)
    for i_elem in filenames:
        if i_elem.endswith('.py'):
            i_path = os.path.abspath(os.path.join(dirpath, i_elem))
            with open(i_path, 'r', encoding='utf-8') as file:
                quotes = 0
                for i_line in file:
                    quotes += i_line.count('"""')
                    if not all(i_sym == ' ' or i_sym == '\n' or i_sym == '' for i_sym in i_line) and \
                            i_line[0] != '#' and quotes % 2 == 0:
                        summ += 1
            print(i_path)
print('Колличество строк в дериктории: ', summ)
