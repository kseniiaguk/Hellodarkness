from math import sqrt

ones = ([1, 0],
        [0, 1])


def rosenbrock(x, y):
    return 5 * (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def himmelblau(x, y):
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2


def gradient(f):
    delta = 8e-15
    x_deriv = lambda x, y: (f(x + delta, y) - f(x, y)) / delta
    y_deriv = lambda x, y: (f(x, y + delta) - f(x, y)) / delta
    return lambda x, y: (x_deriv(x, y), y_deriv(x, y))


def vector_module(x, y):
    return sqrt(x ** 2 + y ** 2)


def scalar_prod(x_1, y_1, x_2, y_2):
    return x_1 * x_2 + y_1 * y_2


def matrix_prod(x_1, y_1, x_2, y_2):
    return ([x_1 * x_2, x_1 * y_2],
            [y_1 * x_2, y_1 * y_2])


def matrix_mul(matrix_1, matrix_2):
    first = matrix_1[0][0] * matrix_2[0][0] + matrix_1[0][1] * matrix_2[1][0]
    second = matrix_1[0][0] * matrix_2[0][1] + matrix_1[0][1] * matrix_2[1][1]
    third = matrix_1[1][0] * matrix_2[0][0] + matrix_1[1][1] * matrix_2[1][0]
    fourth = matrix_1[1][0] * matrix_2[0][1] + matrix_1[1][1] * matrix_2[1][1]
    return ([first, second],
            [third, fourth])


def matrix_sub(matrix_1, matrix_2):
    return ([matrix_1[0][0] - matrix_2[0][0], matrix_1[0][1] - matrix_2[0][1]],
            [matrix_1[1][0] - matrix_2[1][0], matrix_1[1][1] - matrix_2[1][1]])


def matrix_add(matrix_1, matrix_2):
    return ([matrix_1[0][0] + matrix_2[0][0], matrix_1[0][1] + matrix_2[0][1]],
            [matrix_1[1][0] + matrix_2[1][0], matrix_1[1][1] + matrix_2[1][1]])


def vector_prod(matrix, x, y):
    return (scalar_prod(matrix[0][0], matrix[0][1], x, y),
            scalar_prod(matrix[1][0], matrix[1][1], x, y))


def division(matrix, scalar):
    return ([matrix[0][0] / scalar, matrix[0][1] / scalar],
            [matrix[1][0] / scalar, matrix[1][1] / scalar])


def golden_ratio(f, left, right, eps):
    ratio_value = (sqrt(5) + 1) / 2

    len = right - left
    ratio_len_1 = len / ratio_value
    ratio_len_2 = len - ratio_len_1
    l_point = right - ratio_len_1
    r_point = left + ratio_len_1
    l_val = f(l_point)
    r_val = f(r_point)

    while len > eps:
        ratio_len_3 = ratio_len_1 - ratio_len_2
        ratio_len_1 = ratio_len_2
        ratio_len_2 = ratio_len_3

        if (l_val < r_val):
            right = r_point
            r_point = l_point
            r_val = l_val
            l_point = left + ratio_len_2
            l_val = f(l_point)
        elif (r_val <= l_val):
            left = l_point
            l_point = r_point
            l_val = r_val
            r_point = right - ratio_len_2
            r_val = f(r_point)
        len = right - left
    return (right + left) / 2


def matrix_update(matrix, old_x_0, old_y_0, x_0, y_0,
                  old_x_direction, old_y_direction,
                  x_direction, y_direction):
    x_grad_difference = -x_direction + old_x_direction
    y_grad_difference = -y_direction + old_y_direction
    x_point_difference = old_x_0 - x_0
    y_point_difference = old_y_0 - y_0
    scalar = scalar_prod(x_point_difference, y_point_difference, x_grad_difference, y_grad_difference)
    left = matrix_sub(ones,
                      division(matrix_prod(
                          x_grad_difference, y_grad_difference,
                          x_point_difference, y_point_difference),
                          scalar))
    right = matrix_sub(ones,
                       division(matrix_prod(
                           x_point_difference, y_point_difference,
                           x_grad_difference, y_grad_difference),
                           scalar))
    to_add = division(matrix_prod(x_point_difference, y_point_difference,
                                  x_point_difference, y_point_difference),
                      scalar)
    return matrix_add(matrix_mul(matrix_mul(left, matrix), right), to_add)


def optimize(f, x_0, y_0, eps):
    grad = gradient(f)
    matrix = ones
    x_direction, y_direction = vector_prod(matrix, *grad(x_0, y_0))
    x_direction, y_direction = -x_direction, -y_direction

    counter = 0
    while grad(x_0, y_0) != (0, 0):
        counter += 1

        single_arg_func = lambda alpha: f(x_0 + alpha * x_direction, y_0 + alpha * y_direction)
        alpha = golden_ratio(single_arg_func, 0, 100, eps)

        old_x_0 = x_0
        old_y_0 = y_0
        x_0 += alpha * x_direction
        y_0 += alpha * y_direction

        old_x_direction = x_direction
        old_y_direction = y_direction
        x_direction, y_direction = grad(x_0, y_0)
        x_direction, y_direction = -x_direction, -y_direction

        matrix = matrix_update(matrix, old_x_0, old_y_0, x_0, y_0,
                               old_x_direction, old_y_direction,
                               x_direction, y_direction)

        x_direction, y_direction = vector_prod(matrix, x_direction, y_direction);
        x_direction, y_direction = -x_direction, -y_direction

        cond_1 = vector_module(x_0 - old_x_0, y_0 - old_y_0)
        cond_2 = vector_module(x_direction, y_direction)
        if max(cond_1, cond_2) <= eps:
            break
    return ([x_0, y_0], f(x_0, y_0), counter)


def main():
    print("КВАЗИНЬЮТОНОВСКИЙ МЕТОД:")
    # print("---Розенброк-------------------------------------")
    #print("Функция 100(y-x^2)^2+5(1-x)^2 достигает в точке ", optimize(rosenbrock, 2, 1, 1e-5)[0], "минимума",
    #    optimize(rosenbrock, 2, 1, 1e-5)[1], "кол-во итераций:", optimize(rosenbrock, 2, 1, 1e-5)[2])  # (-1, 1)
    print("---Химмельблау-------------------------------------")
    print("Функция (x^2+y-11)^2+(x+y^2-7)^2 достигает в точке ", optimize(himmelblau, -1, 5, 1e-6)[0], "минимума",
          optimize(himmelblau, 0, 0, 1e-6)[1], ", кол-во итераций:", optimize(himmelblau, 0, 0, 1e-6)[2])  # 1,0/ncf


if __name__ == "__main__":
    main()