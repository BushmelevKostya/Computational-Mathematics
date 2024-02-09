import random


class Randomizer:
    def __init__(self, dim):
        self.dim = dim

    def generate_matrix(self):
        matrix = []
        for i in range(self.dim):
            arr = []
            for j in range(self.dim):
                arr.append(random.randint(-99, 99))
            matrix.append(arr)
        return matrix

    def generate_vars(self):
        arr_vars = []
        for i in range(self.dim):
            arr_vars.append(random.randint(-99, 99))
        return arr_vars
