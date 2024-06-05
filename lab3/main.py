import math

from lab6.methods import *
from math import exp, sin, cos


def f_1(x, y):

    return f, exact_y


# '1. y + (1 + x)*y^2'
# '2. x + y'
# '3. sin(x) - y'
n = 1
if n == 1:
    f = lambda x, y: y + (1 + x) * y ** 2
    exact_y = lambda x, x0, y0: -exp(x) / (x * exp(x) - (x0 * exp(x0) * y0 + exp(x0)) / y0)
elif n == 2:
    f = lambda x, y: x + y
    exact_y = lambda x, x0, y0: exp(x - x0) * (y0 + x0 + 1) - x - 1
else:
    f = lambda x, y: sin(x) - y
    exact_y = lambda x, x0, y0: (2 * exp(x0) * y0 - exp(x0) * sin(x0) + exp(x0) * cos(x0)) / (2 * exp(x)) + (
        sin(x)) / 2 - (cos(x)) / 2
y0 = -1
x0, xn = 1, 1.5
h = 0.1
n = 6
eps = 0.01
run_methods(f, exact_y, x0, xn, y0, h, eps, n)
# res = euler_method(f_3, x0, xn, y0, h, eps)
# print(res[0])
# print(res[1])
# res = fourth_order_runge_kutta_method(f_3, x0, xn, y0, h, eps)
# print(res[0])
# print(res[1])
# res = milne_method(f_3, x0, xn, y0, h, eps)
# print(res[0])
# print(res[1])
