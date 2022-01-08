numbers = [1, 10, 0, 3, 5, 0, 7, 2, 0, 4]
new_numbers = [x for x in numbers if x != 0]
diff = len(numbers) - len(new_numbers)
new_numbers = new_numbers + [0 for x in range(diff)]
print('Новый список: ', new_numbers)
for i in range(diff):
    for j in new_numbers:
        if j == 0:
            new_numbers.remove(0)

print('Сжатый список: ', new_numbers)

# зачёт!
