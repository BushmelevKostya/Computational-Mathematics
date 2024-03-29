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
                while 1:
                    print("Enter number of system:\n"
                          "1 - f(x) = x^3 + 2.84x^2-5.606x-14.766\n"
                          "2 - f(x) = x^5 - 8*x^2 - 4\n"
                          "3 - f(x) = 2^x - cos(x) - 3\n"
                          ">>>", end=" ")
                    s = input().strip()
                    if s == "1":
                        dim = 3
                        inp = self.all_input(2)
                        borders = [inp[0], inp[1]]
                        error = inp[2]
                        coefficients = [-14.766, -5.606, 2.84, 1]
                        if self.model.check_roots(coefficients, borders):
                            self.model.do_task(borders, coefficients, dim, error, inp[3])
                        else:
                            print("There are no roots on your interval!")
                            continue
                        break
                    elif s == "2":
                        dim = 5
                        inp = self.all_input(2)
                        approx = [inp[0], inp[1]]
                        error = inp[2]
                        coefficients = [-4, 0, -8, 0, 0, 1]
                        if self.model.check_roots(coefficients, approx):
                            self.model.do_task(approx, coefficients, dim, error, inp[3])
                        else:
                            print("There are no roots on your interval!")
                            continue
                        self.model.do_task(approx, coefficients, dim, error, inp[3])
                        break
                    elif s == "3":
                        dim = 6
                        inp = self.all_input(2)
                        approx = [inp[0], inp[1]]
                        error = inp[2]
                        coefficients = self.model.create_polinim(1)
                        if self.model.check_roots(coefficients, approx):
                            self.model.do_task(approx, coefficients, dim, error, inp[3])
                        else:
                            print("There are no roots on your interval!")
                            continue
                        self.model.do_task(approx, coefficients, dim, error, inp[3])
                        break
                    else:
                        print("Wrong value!")
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
                        inp = self.all_input(2)
                        approx = [inp[0], inp[1]]
                        error = inp[2]
                        self.model.Newton_alg(approx, error, 3)
                        break
                    elif s == "2":
                        inp = self.all_input(2)
                        approx = [inp[0], inp[1]]
                        error = inp[2]
                        self.model.Newton_transcendental_alg(approx, error, 3)
                        break
                    else:
                        continue
                break
            else:
                print("Please enter:\n1 for linear equaiton\n2 for unlinear equation\n>>>", end=" ")

    def all_input(self, dim):
        print(
            "Please enter how to set interval or approximate and error:\n1 for independent input\n2 for file input\n>>>",
            end=" ")
        s = input().strip()
        while 1:
            print("Please enter method:\n"
                  "1 - bisection\n"
                  "2 - secant\n"
                  "3 - simple iteration\n>>>",
                  end=" ")
            try:
                number = int(input())
                if number != 1 and number != 2 and number != 3:
                    continue
                break
            except ValueError:
                print("Wrong value!")
        all_input = [0, 0, 0, number]
        if s == "1":
            while (1):
                try:
                    print(
                        "Please enter interval or approximate with enter. Function must be monotone on interval."
                        " For simple interval method set start approximation twice\n>>>",
                        end=" ")
                    all_input[0], all_input[1] = float(input().strip().replace(",", ".")), float(
                        input().strip().replace(",", "."))
                    break
                except ValueError as e:
                    print("Wrong value, please enter float number")
            while (1):
                try:
                    print("Please enter error\n>>>", end=" ")
                    all_input[2] = float(input().strip().replace(",", "."))
                    break
                except ValueError as e:
                    print("Wrong value, please enter float number")
        elif s == "2":
            while 1:
                print("Please enter name of file\n>>>", end=" ")
                s = input().strip()
                if s == "":
                    continue
                path = "input/" + s
                fileReader = FileReader(path)
                try:
                    approx = fileReader.read_vars(dim)
                    all_input[0], all_input[1] = approx[0], approx[1]
                    all_input[2] = fileReader.read_vars(1)[0]
                    break
                except FileNotFoundError as e:
                    print(e.args[0])
        return all_input
