import math

from Randomizer import *
from FileReader import *
from Model import *


class Executor:
    def __init__(self):
        self.dim = 1
        self.matrix = [[1]]
        self.arr_var = [1]

    def say_hello(self):
        print("Hello! Please enter:\n1 for independent input\n2 for file input\n>>>", end=" ")
        while 1:
            s = input().strip()
            if s == "1":
                print("Enter dimension of matrix, 1 <= dim <= 20\n>>>", end=" ")
                while 1:
                    try:
                        dim = int(input())
                        if dim < 1 or dim > 20:
                            raise ValueError
                        break
                    except ValueError:
                        print("Dimension must be a integer number from 1 to 20")
                self.dim = dim
                print("Enter:\n1 for automatic matrix generation\n2 for independent input\n>>>", end=" ")
                while 1:
                    s = input().strip()
                    if s == "1":
                        randomizer = Randomizer(dim)
                        self.matrix = randomizer.generate_matrix()
                        self.arr_var = randomizer.generate_vars()
                        break
                    elif s == "2":
                        matrix = [[0.0] * dim for _ in range(dim)]
                        arr_var = [0.0] * dim
                        model = Model(dim, matrix, arr_var)
                        model.print_task(matrix, arr_var)
                        print("Enter the coefficients of matrix using enter\n>>>", end=" ")
                        for i in range(dim):
                            for j in range(dim):
                                while 1:
                                    try:
                                        s = float(input())
                                        if math.isinf(s):
                                            raise ArithmeticError("Value is too big")
                                        matrix[i][j] = s
                                        break
                                    except ValueError:
                                        print("Coefficient must be a number")
                                    except ArithmeticError as e:
                                        print(str(e))
                                model.print_task(matrix, arr_var)
                        self.matrix = matrix
                        print("Enter the variables using enter\n>>>", end=" ")
                        for i in range(dim):
                            while 1:
                                try:
                                    s = float(input())
                                    if math.isinf(s):
                                        raise ArithmeticError("Value is too big")
                                    arr_var[i] = s
                                    break
                                except ValueError:
                                    print("Variable must be a number")
                                except ArithmeticError as e:
                                    print(str(e))
                            model.print_task(matrix, arr_var)
                        self.arr_var = arr_var
                        break
                    else:
                        print("Enter:\n1 for automatic matrix generation\n2 for independent input\n>>>", end=" ")
                break
            elif s == "2":
                while 1:
                    print("Enter name of file\n>>>", end=" ")
                    s = input().strip()
                    if s == "":
                        continue
                    path = "input/" + s
                    fileReader = FileReader(path)
                    try:
                        dim = fileReader.read_dim()
                        self.dim = dim
                        self.matrix = fileReader.read_matrix(dim)
                        self.arr_var = fileReader.read_vars()
                        break
                    except FileNotFoundError as e:
                        print(e.args[0])
                break
            else:
                print("Please enter:\n1 for independent input\n2 for file input\n>>>", end=" ")

    def do_task(self):
        dim = self.dim
        matrix = self.matrix
        arr_var = self.arr_var

        model = Model(dim, matrix, arr_var)
        print("Input dimension:", dim, "\n")
        print("Input matrix:")
        model.print_task(matrix, arr_var)
        print("Determinant:", model.det(), "\n")
        results = model.G_alg()
        print("Values of answers:")
        model.print_answers(results)
        errors = model.calc_errors(results)
        print("Values of errors:")
        for i in range(dim):
            print("e", i + 1, " = ", errors[i], sep="")
        print()
