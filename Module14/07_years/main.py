beginning = int(input('Введите первый год: '))
ending = int(input('Введите второй год: '))

first = 0
second = 0
third = 0
fourth = 0

for year in range(beginning, ending + 1):
    first = year // 1000
    second = year // 100 % 10
    third = year // 10 % 10
    fourth = year % 10
    if first == second == third or first == second == fourth or first == fourth == third or fourth == second == third:
        print(year)

# Ok
