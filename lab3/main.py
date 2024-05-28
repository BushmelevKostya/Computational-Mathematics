from lab5.interpolation import *
from lab5.polinoms import *


def func_to_pairs(func, borders, count):
    step = (borders[1] - borders[0]) / (count - 1)
    pairs = [[borders[0] + i * step, func(borders[0] + i * step)] for i in range(count)]
    return pairs


def my_func_1(x):
    return math.exp(x)


def my_func_2(x):
    return x ** 2


borders = [0, 1]
count = 5
pairs = func_to_pairs(my_func_1, borders, count)
pairs = [[0.1, 1.25], [0.2, 2.38], [0.3, 3.79], [0.4, 5.44], [0.5, 7.14]]
print(pairs)
x = 0.11
run_methods(pairs, x)
# poly_str1 = "(x-1)"
# poly_str2 = "(x-1)"
# res1 = parse_polynomial(poly_str1)
# res2 = parse_polynomial(poly_str2)
# print(res1)
# print(res2)
# result = multiply_polynomial_strings(poly_str1, poly_str2)
# print(result)
