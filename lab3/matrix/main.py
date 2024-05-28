from fractions import Fraction


def print_matrix():
    m = [[len(str(x)) for x in matrix[0]], [len(str(x)) for x in matrix[1]], [len(str(x)) for x in matrix[2]],
         [len(str(x)) for x in matrix[3]]]
    sl = max(map(max, m))
    for i in range(len(matrix)):
        for x in matrix[i]:
            s = str(x) + ' ' * (sl - len(str(x)))
            print(s, end='\t')
        print()
    print()


def add_scaled_row(source_row: int, target_row: int, factor: Fraction):
    matrix[target_row] = [x + y * factor for x, y in zip(matrix[target_row], matrix[source_row])]


def scale_row(row, factor):
    matrix[row] = [x * factor for x in matrix[row]]


# matrix = [
#     [Fraction(x) for x in [6, 3, -1, 1, 6, 1, 1, 0, 0]],
#     [Fraction(x) for x in [6, 1, 0, 5, 1, -7, 0, 1, 0]],
#     [Fraction(x) for x in [6, 1, 2, 3, 1, 1, 0, 0, 1]],
#     [Fraction(x) for x in [18, 5, 1, 9, 8, -5, 0, 0, 0]]
# ]
# print_matrix()
#
# scale_row(0, Fraction(1, 6))
# add_scaled_row(0, 1, Fraction(-1, 1))
# add_scaled_row(0, 2, Fraction(-1, 1))
# add_scaled_row(0, 3, Fraction(-8, 1))
#
# print_matrix()
#
# scale_row(1, Fraction(6, 29))
# add_scaled_row(1, 0, Fraction(-1, 6))
# add_scaled_row(1, 2, Fraction(-17, 6))
# add_scaled_row(1, 3, Fraction(-23, 3))
#
# print_matrix()
#
# scale_row(2, Fraction(29, 6))
# add_scaled_row(2, 0, Fraction(-14, 29))
# add_scaled_row(2, 1, Fraction(-3, 29))
# add_scaled_row(2, 3, Fraction(-6, 29))
#
# print_matrix()

matrix = [
    [Fraction(x) for x in [-4, 0, -5, 0, 1, Fraction(-34, 3)]],
    [Fraction(x) for x in [0, 0, -1, 1, 0, -4]],
    [Fraction(x) for x in [10, 1, 10, 0, 0, Fraction(73, 3)]],
    [Fraction(x) for x in [4, 0, -2, 0, 0, Fraction(22, 3)]]
]
print_matrix()

scale_row(2, Fraction(3, 73))
add_scaled_row(2, 0, Fraction(34, 3))
add_scaled_row(2, 1, Fraction(4, 1))
add_scaled_row(2, 3, Fraction(-22, 3))

print_matrix()
