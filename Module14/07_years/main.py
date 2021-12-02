# TODO здесь писать код
beginning = int(input('Введите первый год: '))
ending = int(input('Введите второй год: '))

def numbers(year, number):
    count = 0
    while year != 0:
        if year % 10 == number:
            count += 1
            year //= 10
        else:
            year //= 10
    return count


identical = 0
for year in range(beginning, ending + 1):
    for number in range(10):
        identical = numbers(year, number)
        if identical >= 3:
            print(year)
        else:
            continue