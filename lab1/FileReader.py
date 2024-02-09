class FileReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_matrix(self, dim):
        matrix = []
        try:
            with open(self.filepath, "r") as file:
                file.readline()
                for i in range(dim):
                    data = list(map(int, file.readline().split(" ")))
                    matrix.append(data)
            return matrix
        except FileNotFoundError:
            raise FileNotFoundError("This file doesn't exist! Try another name of file")
        except PermissionError:
            raise FileNotFoundError("You haven't enough permissions for read this file! Try another name of file")

    def read_vars(self):
        try:
            with open(self.filepath, "r") as file:
                data = list(map(int, file.readlines()[-1].strip().split(" ")))
            return data
        except FileNotFoundError:
            raise FileNotFoundError("This file doesn't exist! Try another name of file")
        except PermissionError:
            raise FileNotFoundError("You haven't enough permissions for read this file! Try another name of file")

    def read_dim(self):
        try:
            with open(self.filepath, "r") as file:
                data = int(file.readline())
            return data
        except FileNotFoundError:
            raise FileNotFoundError("This file doesn't exist! Try another name of file")
        except PermissionError:
            raise FileNotFoundError("You haven't enough permissions for read this file! Try another name of file")
