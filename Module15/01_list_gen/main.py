odd_numbers = []
number = int(input('Введите число: '))
for num in range(1, number, 2):
    odd_numbers.append(num)
print(odd_numbers)