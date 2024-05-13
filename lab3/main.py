import math

from lab4.approximation import *
from lab4.output import *

if __name__ == '__main__':
    linear_pairs = [[1.2, 7.4], [2.9, 9.5], [4.1, 11.1], [5.5, 12.9], [6.7, 14.6], [7.8, 17.3], [9.2, 18.2], [10.3, 20.7]]
    polinom_2_pairs = [[1.1, 3.5], [2.3, 4.1], [3.7, 5.2], [5.4, 8.3], [6.8, 14.8], [7.5, 21.2]]
    polinom_3_pairs = [[1, 1], [2, 8], [3, 27], [4, 64], [5, 125], [6, 216]]
    power_pairs = [[1, 2], [2, 16], [3, 54], [4, 128], [5, 250], [6, 400]]
    answers = power_approx(power_pairs)
    power_output(answers)