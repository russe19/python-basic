list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def search_number(list_1, list_2, to_find):
    for x in list_1:
        for y in list_2:
            result = x * y
            yield x, y, result
            if result == to_find:
                print('\nFound!!!')
                return


search = search_number(list_1, list_2, to_find)
for i in search:
    print()
    for i_elem in i:
        print(i_elem, end=' ')
