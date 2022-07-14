from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]


def square_and_round(num: float) -> float:
    num_th = num ** 3
    return round(num_th, 3)


def multi(a: int, b: int) -> int:
    result = a * b
    return result


floats_final = list(map(lambda elem: square_and_round(elem), floats))
names_final = list(filter(lambda elem: len(elem) >= 5, names))
numbers_final = reduce(multi, numbers)

print(floats_final)
print(names_final)
print(numbers_final)
