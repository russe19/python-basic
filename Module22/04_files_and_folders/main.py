def weights(my_path, files, dirs, weights_all):
    paths = os.listdir(my_path)
    for i_elem in paths:
        s = os.path.isdir(os.path.join(my_path, i_elem))
        if os.path.isdir(os.path.join(my_path, i_elem)):
            dirs += 1
            files, dirs, weights_all = weights(os.path.join(my_path, i_elem), files, dirs, weights_all)
        else:
            files += 1
            my_weight = os.path.getsize(os.path.join(my_path, i_elem))
            weights_all += my_weight
    return files, dirs, weights_all


import os

files = 0
dirs = 0
weights_all = 0
path = os.path.abspath('..')
files, dirs, weights_all = weights(path, files, dirs, weights_all)
print(path)
print('Размер каталога (в Кб):', weights_all / 1024)
print('Количество подкаталогов:', dirs)
print('Количество файлов:', files)
