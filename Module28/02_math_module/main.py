from abc import ABC, abstractmethod
import math


class MyMath(ABC):

    @abstractmethod
    def circle_len(radius):
        return 2 * radius * math.pi

    @abstractmethod
    def circle_sq(radius):
        return math.pi * radius ** 2

    @abstractmethod
    def cube_vol(a, b, c):
        return a * b * c

    @abstractmethod
    def cube_surface_perimetr(a, b, c):
        return 2 * (a * b + a * c + b * c)

    @abstractmethod
    def surf_area_sphere(radius):
        return 4 * math.pi * radius ** 2

    @abstractmethod
    def ball_vol(radius):
        return (4 / 3) * math.pi * radius ** 3


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_vol(a=5, b=6, c=7)
res_4 = MyMath.cube_surface_perimetr(a=5, b=6, c=7)
res_5 = MyMath.surf_area_sphere(radius=7)
res_6 = MyMath.ball_vol(radius=4)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
print(res_5)
print(res_6)
