def linear_output(answers):
    print("a: ", round(answers[6][0], 2))
    print("b: ", round(answers[6][1], 2))
    print("x_i: ", end="")
    for pair in answers[0]:
        print(round(pair[0], 2), end=" ")
    print()
    print("y_i: ", end="")
    for pair in answers[0]:
        print(round(pair[1], 2), end=" ")
    print()
    print("P(x_i): ", end="")
    for pair in answers[1]:
        print(round(pair[1], 2), end=" ")
    print()
    print("e_i: ", end="")
    for e in answers[2]:
        print(round(e, 2), end=" ")
    print()
    print("sqr_diff: ", round(answers[3], 2))
    print("pirson_coef: ", round(answers[4], 3))
    print("det_coef: ", round(answers[5], 3), " - ", end="")
    if answers[5] >= 0.95:
        print("high accuracy!")
    elif 0.75 <= answers[5] <= 0.95:
        print("good accuracy!")
    elif 0.5 <= answers[5] <= 0.75:
        print("weak accuracy!")
    elif answers[5] <= 0.5:
        print("bad accuracy! Try to change approximation model")


def polinom_2_output(answers):
    print("a0: ", round(answers[5][0], 2))
    print("a1: ", round(answers[5][1], 2))
    print("a2: ", round(answers[5][2], 2))
    print("x_i: ", end="")
    for pair in answers[0]:
        print(round(pair[0], 2), end=" ")
    print()
    print("y_i: ", end="")
    for pair in answers[0]:
        print(round(pair[1], 2), end=" ")
    print()
    print("P(x_i): ", end="")
    for pair in answers[1]:
        print(round(pair[1], 2), end=" ")
    print()
    print("e_i: ", end="")
    for e in answers[2]:
        print(round(e, 2), end=" ")
    print()
    print("sqr_diff: ", round(answers[3], 2))
    print("det_coef: ", round(answers[4], 3), " - ", end="")
    if answers[4] >= 0.95:
        print("high accuracy!")
    elif 0.75 <= answers[4] <= 0.95:
        print("good accuracy!")
    elif 0.5 <= answers[4] <= 0.75:
        print("weak accuracy!")
    elif answers[4] <= 0.5:
        print("bad accuracy! Try to change approximation model")


def polinom_3_output(answers):
    print("a0: ", round(answers[5][0], 2))
    print("a1: ", round(answers[5][1], 2))
    print("a2: ", round(answers[5][2], 2))
    print("a3: ", round(answers[5][3], 2))
    print("x_i: ", end="")
    for pair in answers[0]:
        print(round(pair[0], 2), end=" ")
    print()
    print("y_i: ", end="")
    for pair in answers[0]:
        print(round(pair[1], 2), end=" ")
    print()
    print("P(x_i): ", end="")
    for pair in answers[1]:
        print(round(pair[1], 2), end=" ")
    print()
    print("e_i: ", end="")
    for e in answers[2]:
        print(round(e, 2), end=" ")
    print()
    print("sqr_diff: ", round(answers[3], 2))
    print("det_coef: ", round(answers[4], 3), " - ", end="")
    if answers[4] >= 0.95:
        print("high accuracy!")
    elif 0.75 <= answers[4] <= 0.95:
        print("good accuracy!")
    elif 0.5 <= answers[4] <= 0.75:
        print("weak accuracy!")
    elif answers[4] <= 0.5:
        print("bad accuracy! Try to change approximation model")


def power_output(answers):
    print("a: ", round(answers[5][0], 2))
    print("b: ", round(answers[5][1], 2))
    print("x_i: ", end="")
    for pair in answers[0]:
        print(round(pair[0], 2), end=" ")
    print()
    print("y_i: ", end="")
    for pair in answers[0]:
        print(round(pair[1], 2), end=" ")
    print()
    print("P(x_i): ", end="")
    for pair in answers[1]:
        print(round(pair[1], 2), end=" ")
    print()
    print("e_i: ", end="")
    for e in answers[2]:
        print(round(e, 2), end=" ")
    print()
    print("sqr_diff: ", round(answers[3], 2))
    print("det_coef: ", round(answers[4], 3), " - ", end="")
    if answers[4] >= 0.95:
        print("high accuracy!")
    elif 0.75 <= answers[4] <= 0.95:
        print("good accuracy!")
    elif 0.5 <= answers[4] <= 0.75:
        print("weak accuracy!")
    elif answers[4] <= 0.5:
        print("bad accuracy! Try to change approximation model")
