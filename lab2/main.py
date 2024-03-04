from Executor import *
from SLAEModel import *

if __name__ == '__main__':
    executor = Executor()
    model = SLAEModel()
    equation = "x^3 + 2.84x^2-5.606x-14.766"
    coefficients = [-14.766, -5.606, 2.84, 1]
    borders = [2, 3]
    error = 0.01

    model.bisection_alg(borders, coefficients, 3, error)

    approx = [2, 3]
    model.secant_alg(approx, coefficients, 3, error)

    coefficients = [-14.766, -5.606, 2.84, 1]
    new_coefficients = [14.766, 5.606, -2.84]
    approx = [-4, 0]
    degree = 1 / 3
    model.simple_iteration_alg(approx, coefficients, new_coefficients, 3, degree, error)
