def disclosure(in_list, new_list):
    for elem in in_list:
        if isinstance(elem, int):
            new_list.append(elem)
        if isinstance(elem, list):
            disclosure(elem, new_list)
    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
new_list = []

disclosure(nice_list, new_list)
print(new_list)
