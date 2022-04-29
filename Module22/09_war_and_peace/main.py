import os
import zipfile


def unzip(file):
    file = zipfile.ZipFile('voyna-i-mir.zip', 'r')
    for i_zip in file.namelist():
        file.extract(i_zip)
    file.close()


def count_latters_func(file_name):
    result = {}
    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))
    text_file = open(file_name, 'r', encoding='utf-8')
    for i_line in text_file:
        for i_char in i_line:
            if i_char.isalpha():
                if i_char not in result:
                    result[i_char] = 0
                result[i_char] += 1
    text_file.close()

    return result


def print_stats(stats):
    print("+{:-^19}+".format('+'))
    print("|{: ^9}|{: ^9}|".format('буква', 'число'))
    print("+{:-^19}+".format('+'))
    for char, count in stats.items():
        print("|{: ^9}|{: ^9}|".format(char, count))
    print("+{:-^19}+".format('+'))


def sort_by_frequence(stats):
    sorted_values = sorted(stats.values(), reverse=True)
    sorted_dict = dict()
    for i_value in sorted_values:
        for i_key in stats.keys():
            if stats[i_key] == i_value:
                sorted_dict[i_key] = stats[i_key]

    return sorted_dict


stats = count_latters_func('voyna-i-mir.zip')
stats = sort_by_frequence(stats)
print_stats(stats)
