import math

from Model import *

class SLAEModel:

    def print_answers(self, dim, arr_var):
        for i in range(dim):
            print("x", i + 1, " = ", round(arr_var[i], 5), sep="")
        print()

    def calc_func(self, coefficients, dim, dot):
        res = 0
        for i in range(dim + 1):
            res += coefficients[i] * dot ** i

        return res

    def bisection_alg(self, borders, coefficients, dim, error):
        n = 0
        x = (borders[0] + borders[1]) / 2
        while abs(borders[0] - borders[1]) > error and abs(self.calc_func(coefficients, dim, x)) >= error:
            x = (borders[0] + borders[1]) / 2
            if self.calc_func(coefficients, dim, borders[0]) * self.calc_func(coefficients, dim, x) > 0:
                borders[0] = x
            else:
                borders[1] = x
            n += 1
        x = (borders[0] + borders[1]) / 2
        self.print_answers(dim, [x, self.calc_func(coefficients, dim, x), n])

    def secant_alg(self, approx, coefficients, dim, error):
        n = 0
        func_values = [self.calc_func(coefficients, dim, approx[0]), self.calc_func(coefficients, dim, approx[1])]
        while abs(approx[1] - approx[0]) > error and abs(self.calc_func(coefficients, dim, approx[1])):
            derivative = (func_values[1] - func_values[0]) / (approx[1] - approx[0])
            next_x = approx[1] - self.calc_func(coefficients, dim, approx[1]) / derivative
            approx[0], approx[1] = approx[1], next_x
            next_y = self.calc_func(coefficients, dim, approx[1])
            func_values[0], func_values[1] = func_values[1], next_y
            n += 1
        self.print_answers(dim, [approx[1], self.calc_func(coefficients, dim, approx[1]), n])

    def simple_iteration_alg(self, approx, coefficients, new_coefficients, dim, degree, error):
        n = 1
        while 1:
            res_func = self.calc_func(new_coefficients, len(new_coefficients) - 1, approx[0])
            if res_func < 0:
                approx[1] = - (abs(res_func) ** degree)
            else:
                approx[1] = abs(res_func) ** degree

            if abs(approx[1] - approx[0]) < error:
                break
            approx[0] = approx[1]
            n += 1
        self.print_answers(dim, [approx[1], self.calc_func(coefficients, dim, approx[1]), n])

    def simple_iteration_transcendental_alg(self, approx, error):
        n = 1
        while 1:
            approx[1] = math.log2(math.cos(approx[0]) + 3)
            if abs(approx[1] - approx[0]) < error:
                break
            approx[0] = approx[1]
            n += 1
        self.print_answers(2, [approx[1], n])

    def Newton_alg(self, approx, error, dim):
        coefficients = [[0, 0], [0, 0]]
        arr_values = [0, 0]
        n = 1
        while 1:
            coefficients[0][0], coefficients[0][1], coefficients[1][0], coefficients[1][1] = 2 * approx[0], 2 * approx[
                1], -6 * approx[0], 1
            arr_values[0], arr_values[1] = 4 - approx[0] ** 2 - approx[1] ** 2, 3 * approx[0] ** 2 - approx[1]
            model = Model(2, coefficients, arr_values)
            temp = approx
            approx[0], approx[1] = approx[0] + model.G_alg()[0], approx[1] + model.G_alg()[1]
            if abs(approx[0] - temp[0]) <= error and abs(approx[1] - temp[1]) <= error:
                break
            n += 1
        self.print_answers(dim, [approx[0], approx[1], n])

    def Newton_transcendental_alg(self, approx, error, dim):
        coefficients = [[0, 0], [0, 0]]
        arr_values = [0, 0]
        n = 1
        while 1:
            coefficients[0][0], coefficients[0][1], coefficients[1][0], coefficients[1][1] = (math.sin(approx[0]) - 1,
                                                                                              0, 0, - math.sin(approx[1]))
            arr_values[0], arr_values[1] = -0.5 + approx[1] + math.cos(approx[0] - 1), -3 + approx[0] - math.cos(approx[1])
            model = Model(2, coefficients, arr_values)
            temp = approx
            approx[0], approx[1] = approx[0] + model.G_alg()[0], approx[1] + model.G_alg()[1]
            if abs(approx[0] - temp[0]) <= error and abs(approx[1] - temp[1]) <= error:
                break
            n += 1
        self.print_answers(dim, [approx[0], approx[1], n])