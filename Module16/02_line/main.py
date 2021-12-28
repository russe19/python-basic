first_class = list(range(160, 177, 2))
second_class = list(range(162, 181, 2))

first_class.extend(second_class)

for i in range(len(first_class)):
    for index in range(len(first_class)):
        if first_class[i] <= first_class[index]:
            first_class[i], first_class[index] = first_class[index], first_class[i]
print(first_class)