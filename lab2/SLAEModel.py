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
