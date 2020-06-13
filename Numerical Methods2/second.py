import random
import first as f
import numpy as np
import math
import time
# ------------------------------------------------------------------------------
# ФУНКЦИИ
# ------------------------------------------------------------------------------


def func(vector):
    x1 = vector[0, 0]
    x2 = vector[1, 0]
    x3 = vector[2, 0]
    x4 = vector[3, 0]
    x5 = vector[4, 0]
    x6 = vector[5, 0]
    x7 = vector[6, 0]
    x8 = vector[7, 0]
    x9 = vector[8, 0]
    x10 = vector[9, 0]
    funcs = np.mat([math.cos(x2 * x1) - math.exp(-3 * x3) + x4 * x5 ** 2 - x6 -
                    math.sinh(2 * x8) * x9 + 2 * x10 + 2.000433974165385440,
                    math.sin(x2 * x1) + x3 * x9 * x7 - math.exp(-x10 + x6) + 3 *
                    x5 ** 2 - x6 * (x8 + 1) + 10.886272036407019994, x1 - x2 + x3 -
                    x4 + x5 - x6 + x7 - x8 + x9 - x10 - 3.1361904761904761904,
                    2 * math.cos(-x9 + x4) + x5 / (x3 + x1) - math.sin(x2 ** 2) + math.cos(x7 * x10) ** 2 -
                    x8 - 0.1707472705022304757, math.sin(x5) + 2 * x8 * (x3 + x1) -
                    math.exp(-x7 * (-x10 + x6)) + 2 * math.cos(x2) - 1.0 / (-x9 + x4) - 0.3685896273101277862,
                    math.exp(x1 - x4 - x9) + x5 ** 2 / x8 + math.cos(3 * x10 * x2) / 2 -
                    x6 * x3 + 2.0491086016771875115,
                    x2 ** 3 * x7 - math.sin(x10 / x5 + x8) + (x1 - x6) * math.cos(x4) + x3 - 0.7380430076202798014,
                    x5 * (x1 - 2 * x6) ** 2 - 2 * math.sin(-x9 + x3) + 0.15e1 * x4 -
                    math.exp(x2 * x7 + x10) + 3.5668321989693809040,
                    7 / x6 + math.exp(x5 + x4) - 2 * x2 * x8 * x10 * x7 + 3 * x9 - 3 * x1 - 8.4394734508383257499,
                    x10 * x1 + x9 * x2 - x8 * x3 + math.sin(x4 + x5 + x6) * x7 - 0.78238095238095238096])
    return np.transpose(funcs)


def jacobi_matrix(vector):
    x1 = vector[0, 0]
    x2 = vector[1, 0]
    x3 = vector[2, 0]
    x4 = vector[3, 0]
    x5 = vector[4, 0]
    x6 = vector[5, 0]
    x7 = vector[6, 0]
    x8 = vector[7, 0]
    x9 = vector[8, 0]
    x10 = vector[9, 0]
    j_funcs = np.mat([[-x2 * math.sin(x2 * x1), -x1 * math.sin(x2 * x1), 3 * math.exp(-3 * x3), x5 ** 2, 2 * x4 * x5,
                       -1, 0, -2 * math.cosh(2 * x8) * x9, -math.sinh(2 * x8), 2],
                      [x2 * math.cos(x2 * x1), x1 * math.cos(x2 * x1), x9 * x7, 0, 6 * x5,
                       -math.exp(-x10 + x6) - x8 - 1, x3 * x9, -x6, x3 * x7, math.exp(-x10 + x6)],
                      [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                      [-x5 / (x3 + x1) ** 2, -2 * x2 * math.cos(x2 ** 2), -x5 / (x3 + x1) ** 2, -2 * math.sin(-x9 + x4),
                       1.0 / (x3 + x1), 0, -2 * math.cos(x7 * x10) * x10 * math.sin(x7 * x10), -1,
                       2 * math.sin(-x9 + x4), -2 * math.cos(x7 * x10) * x7 * math.sin(x7 * x10)],
                      [2 * x8, -2 * math.sin(x2), 2 * x8, 1.0 / (-x9 + x4) ** 2, math.cos(x5),
                       x7 * math.exp(-x7 * (-x10 + x6)), -(x10 - x6) * math.exp(-x7 * (-x10 + x6)), 2 * x3 + 2 * x1,
                       -1.0 / (-x9 + x4) ** 2, -x7 * math.exp(-x7 * (-x10 + x6))],
                      [math.exp(x1 - x4 - x9), -1.5 * x10 * math.sin(3 * x10 * x2), -x6, -math.exp(x1 - x4 - x9),
                       2 * x5 / x8, -x3, 0, -x5 ** 2 / x8 ** 2, -math.exp(x1 - x4 - x9), -1.5 * x2 *
                       math.sin(3 * x10 * x2)],
                      [math.cos(x4), 3 * x2 ** 2 * x7, 1, -(x1 - x6) * math.sin(x4), x10 / x5 ** 2 *
                       math.cos(x10 / x5 + x8),
                       -math.cos(x4), x2 ** 3, -math.cos(x10 / x5 + x8), 0, -1.0 / x5 * math.cos(x10 / x5 + x8)],
                      [2 * x5 * (x1 - 2 * x6), -x7 * math.exp(x2 * x7 + x10), -2 * math.cos(-x9 + x3), 1.5,
                       (x1 - 2 * x6) ** 2, -4 * x5 * (x1 - 2 * x6), -x2 * math.exp(x2 * x7 + x10), 0, 2 *
                       math.cos(-x9 + x3),
                       -math.exp(x2 * x7 + x10)],
                      [-3, -2 * x8 * x10 * x7, 0, math.exp(x5 + x4), math.exp(x5 + x4),
                       -7.0 / x6 ** 2, -2 * x2 * x8 * x10, -2 * x2 * x10 * x7, 3, -2 * x2 * x8 * x7],
                      [x10, x9, -x8, math.cos(x4 + x5 + x6) * x7, math.cos(x4 + x5 + x6) * x7,
                       math.cos(x4 + x5 + x6) * x7, math.sin(x4 + x5 + x6), -x3, x2, x1]])
    return j_funcs


def new_system_solution(matrix, vector, p, q, l, u):
    ops = 0
    dim = matrix.shape[0]
    if f.compatibility_check(matrix, u, vector):
        if np.linalg.det(matrix):
            y = np.zeros((dim, 1))
            x = np.zeros((dim, 1))
            bv = p.dot(vector)
            ops += dim ** 2
            for i in range(dim):
                sum_y = 0
                for k in range(i):
                    sum_y += l[i][k] * y[k]
                    ops += 2
                y[i] = bv[i] - sum_y
                ops += 2
            for j in range(dim):
                sum_x = 0
                for k in range(j):
                    sum_x += u[dim - j - 1][dim - k - 1] * x[dim - k - 1]
                    ops += 2
                x[dim - j - 1] = (y[dim - j - 1] - sum_x) / u[dim - j - 1][dim - j - 1]
                ops += 2
            x = q.dot(x)
            ops += dim ** 2
        else:
            ma = u
            mpb = np.linalg.inv(l).dot(p).dot(vector)
            ops += 4 * dim ** 2
            x = np.zeros((dim, 1))
            for i in range(dim):
                if np.sum(np.abs(ma[dim - i - 1])) + mpb[dim - i - 1] != 0:
                    sum_x = 0
                    for k in range(i):
                        sum_x += ma[dim - i - 1, dim - k - 1] * x[dim - k - 1]
                        ops += 2
                    x[dim - i - 1] = (mpb[dim - i - 1] - sum_x) / ma[dim - i - 1][dim - i - 1]
                    ops += 2
                else:
                    x[dim - i - 1] = random.triangular(0, 10)
            x = q.dot(x)
            ops += dim ** 2
    else:
        x = None
    return x, ops


def newton(fun, jac, epsilon, initial_val):
    time.clock()
    iterations = 0
    operations = 0
    x = np.copy(initial_val)
    norm = 1000
    x_est = 0
    while norm > epsilon:
        if norm > 1000 or x_est is None:
            return None, None, None, None
        p, q, l, u = f.full_pivot_lu_dec(jac(x))[1:]
        p = f.p_matrix_formation(p)
        q = f.q_matrix_formation(q)
        iterations += 1
        x_est, ops = new_system_solution(jac(x), -fun(x), p, q, l, u)
        operations += ops
        norm = np.linalg.norm(x_est, np.inf)
        x += x_est
    lasting = time.clock()
    return x, iterations, operations, lasting


def newton_modified(fun, jac, epsilon, initial_val):
    time.clock()
    iterations = 0
    operations = 0
    x = np.copy(initial_val)
    norm = 1000
    jac_0 = jac(x)
    p, q, l, u = f.full_pivot_lu_dec(jac_0)[1:]
    p = f.p_matrix_formation(p)
    q = f.q_matrix_formation(q)
    while norm > epsilon:
        if norm > 1000:
            return None, None, None, None
        iterations += 1
        x_est, ops = new_system_solution(jac_0, -fun(x), p, q, l, u)
        operations += ops
        if x_est is None:
            return None, None, None, None
        norm = np.linalg.norm(x_est, np.inf)
        x += x_est
    lasting = time.clock()
    return x, iterations, operations, lasting


def newton_transition(k, fun, jac, epsilon, initial_val):
    time.clock()
    iterations = 0
    operations = 0
    x = np.copy(initial_val)
    for i in range(k-1):
        s1, p1, q1, l1, u1 = f.full_pivot_lu_dec(jac(x))
        p1 = f.p_matrix_formation(p1)
        q1 = f.q_matrix_formation(q1)
        iterations += 1
        x_est, ops = new_system_solution(jac(x), -fun(x), p1, q1, l1, u1)
        operations += ops
        x += x_est
    x, iter_num, oper_num = newton_modified(func, jacobi_matrix, epsilon, x)[:3]
    if x is None:
        return None, None, None, None
    iterations += iter_num
    operations += oper_num
    lasting = time.clock()
    return x, iterations, operations, lasting


def newton_periodic(k, fun, jac, epsilon, initial_val):
    time.clock()
    iterations = 0
    operations = 0
    x = np.copy(initial_val)
    norm = 1000
    jac_0 = np.copy(jac(x))
    while norm > epsilon:
        iterations += 1
        if not iterations % k:
            jac_0 = np.copy(jac(x))
        p, q, l, u = f.full_pivot_lu_dec(jac_0)[1:]
        p = f.p_matrix_formation(p)
        q = f.q_matrix_formation(q)
        x_est, ops = new_system_solution(jac_0, -fun(x), p, q, l, u)
        operations += ops
        if norm > 1000 or x_est is None:
            return None, None, None, None
        norm = np.linalg.norm(x_est, np.inf)
        x += x_est
    lasting = time.clock()
    return x, iterations, operations, lasting
