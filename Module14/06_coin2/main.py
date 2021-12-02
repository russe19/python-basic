print('Введите координаты монетки: ')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))

if x ** 2 + y ** 2 > r:
    print('Монетки в области нет')
else:
    print('Монетка где-то рядом')