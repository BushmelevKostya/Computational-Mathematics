import math

from Randomizer import *
from FileReader import *
from SLAEModel import *


class Executor:
    def __init__(self):
        self.dim = 1
        self.matrix = [[1]]
        self.arr_var = [1]
        self.model = SLAEModel()

    def say_hello(self):
        print("Hello! Please enter:\n1 for linear equaiton\n2 for unlinear equation\n>>>", end=" ")
        while 1:
            s = input().strip()
            if s == "1":
                print("Enter number of system:\n"
                      "1 - f(x, y) = x^3 + 2.84x^2-5.606x-14.766\n"
                      "2 - f(x) = x^5 - 8*x^2 - 4\n"
                      "3 - f(x) = ln((x-3)^2)-cos(x) + 6\n"
                      ">>>", end=" ")
                while 1:
                    s = input().strip()
                    if s == "1":
                        dim = 3
                        borders = self.input_approx(2)
                        error = self.input_error()
                        coefficients = [-14.766, -5.606, 2.84, 1]
                        self.model.bisection_alg(borders, coefficients, dim, error)
                        break
                    elif s == "2":
                        dim = 5
                        approx = self.input_approx(2)
                        error = self.input_error()
                        coefficients = [-4, 0, -8, 0, 0, 1]
                        self.model.secant_alg(approx, coefficients, dim, error)
                        break
                    elif s == "3":
                        approx = self.input_approx(2)
                        error = self.input_error()
                        self.model.simple_iteration_transcendental_alg(approx, error)
                    else:
                        continue
                break
            elif s == "2":
                while 1:
                    print("Enter number of equation:\n"
                          "1 - f(x, y) = x^2 + y^2 -4, g(x, y) = y - 3 * x^2\n"
                          "2 - f(x, y) = cos(x-1) + y - 0.5, g(x, y) = x - cos(y) - 3\n"
                          ">>>", end=" ")
                    s = input().strip()
                    if s == "1":
                        approx = self.input_approx(2)
                        error = self.input_error()
                        self.model.Newton_alg(approx, error, 3)
                        break
                    elif s == "2":
                        approx = self.input_approx(2)
                        error = self.input_error()
                        self.model.Newton_transcendental_alg(approx, error, 3)
                        break
                    else:
                        continue
                break
            else:
                print("Please enter:\n1 for linear equaiton\n2 for unlinear equation\n>>>", end=" ")

    def input_approx(self, dim):
        print("Please enter interval or approximate:\n1 for independent input\n2 for file input\n>>>", end=" ")
        s = input().strip()
        approx = [0, 0]
        if s == "1":
            approx[0], approx[1] = float(input())
        elif s == "2":
            while 1:
                s = input().strip()
                if s == "":
                    continue
                path = "input/" + s
                fileReader = FileReader(path)
                try:
                    approx = fileReader.read_vars(dim)
                    break
                except FileNotFoundError as e:
                    print(e.args[0])
        return approx

    def input_error(self):
        print("Please enter error:\n1 for independent input\n2 for file input\n>>>", end=" ")
        s = input().strip()
        error = 0
        if s == "1":
            error = float(input())
        elif s == "2":
            while 1:
                s = input().strip()
                if s == "":
                    continue
                path = "input/" + s
                fileReader = FileReader(path)
                try:
                    error = fileReader.read_vars(1)
                    break
                except FileNotFoundError as e:
                    print(e.args[0])
        return error


    def do_task(self):
        dim = self.dim
        matrix = self.matrix
        arr_var = self.arr_var

        model = Model(dim, matrix, arr_var)
        print("Input dimension:", dim, "\n")
        print("Input matrix:")
        model.print_task(matrix, arr_var)
        results = model.G_alg()
        if results == -1:
            return
        print("Values of answers:")
        model.print_answers(results)
        errors = model.calc_errors(results)
        print("Values of errors:")
        for i in range(dim):
            print("e", i + 1, " = ", errors[i], sep="")
        print()
