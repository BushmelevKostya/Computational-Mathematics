def print_diff_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            print(round(matrix[i][j], 2), end=" ")
        print()


def lagrange_output(res, dot):
    print("Lagrange method - result value f(", dot, "): ", round(res, 4))


def newton_output(res, dot):
    print("Newton method - result value f(", dot, "): ", round(res, 4))


def gauss_output(res, dot):
    print("Gauss method - result value f(", dot, "): ", round(res, 4))
