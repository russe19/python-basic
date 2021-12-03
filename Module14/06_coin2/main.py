print('Введите координаты монетки: ')
coordinate_x = float(input('X: '))
coordinate_y = float(input('Y: '))
radius_maximum = float(input('Введите радиус: '))

radius_calculated = coordinate_x ** 2 + coordinate_y ** 2

if radius_calculated > radius_maximum:
    print('Монетки в области нет')
else:
    print('Монетка где-то рядом')
