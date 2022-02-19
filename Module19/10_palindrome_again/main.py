text = input('Введите строку: ')
symbols = {}
for sym in text:
    if sym in symbols:
        symbols[sym] += 1
    else:
        symbols[sym] = 1

sum = 0
for i in symbols.values():
    if i % 2 != 0:
        sum += 1

if sum > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')