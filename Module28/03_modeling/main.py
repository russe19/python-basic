class Square:
    def __init__(self, param):
        self._param = param

    def square_of_square(self) -> int or float:
        return self._param ** 2

    def perimeter(self) -> int or float:
        return self._param * 4

    @property
    def param(self) -> int and float:
        return self._param

    @param.setter
    def param(self, param) -> None:
        self._param = param

    def __str__(self):
        return 'Сторона:{}\tПлощадь:{}\tПериметр:{}'.format(self.param, self.square_of_square(), self.perimeter())


class Triangle:
    def __init__(self, height, length):
        self._length = length
        self._height = height

    def perimeter_triangle(self):
        return self._length * 3

    def square_triangle(self):
        return (self._length * self._height) / 2

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    def __str__(self):
        return 'Основание:{}\tВысота:{}\tПлощадь:{}\tПериметр:{}'.format(
            self.length, self.height, self.square_triangle(), self.perimeter_triangle()
        )


class Cube(Square):

    def __init__(self, value: int):
        super().__init__(value)
        self._one_square = [Square(value) for _ in range(6)]

    def square_cube(self):
        return 6 * self._one_square[0].square_of_square()

    @property
    def length(self):
        return self._one_square

    @length.setter
    def length(self, value):
        for i in range(6):
            self._one_square[i] = Square(value)

    def __str__(self):
        return 'Куб имеет 6 одинаковых квадратов со сторонами {}\tПлощадь поверхности куба {}'.format(
            self.param, self.square_cube())


class Pyramid(Triangle, Square):
    def __init__(self, height: int, triangle_length: int, base: int = 4):
        super().__init__(height, triangle_length)
        self.base = base
        self.piramid = [(Triangle(height, triangle_length) if i < 4 else Square(triangle_length)) for i in
                        range(self.base)]

    def square_pyramid(self):
        if self.base == 4:
            return 4 * self.piramid[0].square_triangle()
        elif self.base == 5:
            return 4 * self.piramid[0].square_triangle() + self.piramid[4].square_of_square()
        else:
            return None

    def __str__(self):
        if self.base == 4:
            return 'Пирамида с треугольником в основании, площадь поверхности:{}, ' \
                   'основание треугольника:{}, высота треугольника:{}'.format(
                self.square_pyramid(), self.length, self.height)
        elif self.base == 5:
            return 'Пирамида с квадратом в основании, площадь поверхности:{}, ' \
                   'основание треугольника и сторона квадрата:{}, высота треугольника:{}'.format(
                self.square_pyramid(), self.length, self.height)
        else:
            return 'None'


print('Квадрат')
sq_1 = Square(6)
print(sq_1)
print('Треугольник')
tr_1 = Triangle(3, 5)
print(tr_1)
print('Куб')
cub_1 = Cube(5)
print(cub_1)
print('Пирамида')
pir_1 = Pyramid(3, 4, 5)
print(pir_1)
