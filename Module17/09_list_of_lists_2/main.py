nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [number for external_list in nice_list for internal_list in external_list for number in internal_list]
print(new_list)