import numpy as np
import random
import math
# ---------------------------------------------------------
# ФУНКЦИИ
# ---------------------------------------------------------


def pivoting(matrix, e):
    dim = matrix.shape[0]
    pivot = -1
    pivot_v = matrix[e][e]
    for row in range(e+1, dim):
        if abs(matrix[row, e]) > abs(pivot_v):
            pivot_v = matrix[row, e]
            pivot = row
    return pivot, pivot_v


def full_pivoting(matrix, e):
    dim = matrix.shape[0]
    pivot_column = -1
    pivot_row = -1
    pivot_v = 0
    for row in range(e, dim):
        for column in range(e, dim):
            if abs(matrix[row, column]) > abs(pivot_v):
                pivot_v = matrix[row, column]
                pivot_column = column
                pivot_row = row
    return pivot_row, pivot_column, pivot_v


def swap_rows(matrix, r1, r2):
    new_matrix = np.copy(matrix)
    new_matrix[r1] = matrix[r2]
    new_matrix[r2] = matrix[r1]
    return new_matrix


def swap_columns(matrix, c1, c2):
    new_matrix = np.copy(matrix)
    new_matrix[:, c1] = matrix[:, c2]
    new_matrix[:, c2] = matrix[:, c1]
    return new_matrix


def lu_decomposing(matrix):
    dim = matrix.shape[0]
    p = np.arange(dim)
    q = np.arange(dim)
    w = np.copy(matrix)
    swaps = 0
    for i in range(dim):
        new_row = pivoting(w, i)[0]
        new_val = pivoting(w, i)[1]
        if new_row != -1:
            swaps += 1
            temp = p[i]
            p[i] = p[new_row]
            p[new_row] = temp
            w = swap_rows(w, i, new_row)
        for j in range(i+1, dim):
            w[j][i] /= new_val
            for m in range(i+1, dim):
                w[j][m] -= w[j][i]*w[i][m]
    l = np.tril(w, k=-1) + np.eye(dim)
    u = np.triu(w)
    return swaps, p, q, l, u


def p_matrix_formation(p):
    dim = p.shape[0]
    ans = np.zeros((dim, dim))
    for i in range(dim):
        ans[i][p[i]] = 1
    return ans


def exist_not_zero_elements(row):
    dim = row.shape[0]
    for i in range(dim):
        if abs(row[i]) - 1e-7 > 0:
            return True
    return False


def sing_mat_rang(matrix):
    dim = matrix.shape[0]
    rang = dim
    for row in range(dim):
        if not exist_not_zero_elements(matrix[dim - row - 1]):
            rang -= 1
    return rang


def upper_triangle_determinant(u, swaps):
    det = 1
    dim = u.shape[0]
    for i in range(dim):
        det *= u[i][i]
    return math.pow(-1, swaps)*det


def matrix_generation():
    dim = random.randint(2, 10)
    a = np.random.sample((dim, dim))
    return a


def system_solution(l, u, b, p):
    dim = b.shape[0]
    y = np.zeros((dim, 1))
    x = np.zeros((dim, 1))
    bv = p.dot(b)
    for i in range(dim):
        sum_y = 0
        for k in range(i):
            sum_y += l[i][k]*y[k]
        y[i] = bv[i] - sum_y
    for j in range(dim):
        sum_x = 0
        for k in range(j):
            sum_x += u[dim - j - 1][dim - k - 1] * x[dim - k - 1]
        x[dim - j - 1] = (y[dim - j - 1] - sum_x) / u[dim - j - 1][dim - j - 1]
    return x


def b_generation(dim):
    b = np.random.sample((dim, 1))
    return b


def inverse_matrix(matrix, l, u, p):
    dim = matrix.shape[0]
    inv_matrix = np.zeros(matrix.shape)
    for i in range(dim):
        e = np.eye(dim, 1, -i)
        inv_matrix[i] = system_solution(l, u, e, p).transpose()
    return inv_matrix.transpose()


def full_pivot_lu_dec(matrix):
    dim = matrix.shape[0]
    p = np.arange(dim)
    q = np.arange(dim)
    w = np.copy(matrix)
    swaps = 0
    for i in range(dim):
        new_row = full_pivoting(w, i)[0]
        new_column = full_pivoting(w, i)[1]
        new_val = full_pivoting(w, i)[2]
        if new_val != 0:
            if new_row != i:
                swaps += 1
                temp = p[i]
                p[i] = p[new_row]
                p[new_row] = temp
                w = swap_rows(w, i, new_row)
            if new_column != i:
                swaps += 1
                temp = q[i]
                q[i] = q[new_column]
                q[new_column] = temp
                w = swap_columns(w, i, new_column)
            for j in range(i + 1, dim):
                w[j][i] /= new_val
                for m in range(i + 1, dim):
                    w[j][m] -= w[j][i] * w[i][m]
    l = np.tril(w, k=-1) + np.eye(dim)
    u = np.triu(w)
    return swaps, p, q, l, u


def q_matrix_formation(q):
    dim = q.shape[0]
    ans = np.zeros((dim, dim))
    for i in range(dim):
        ans[q[i]][i] = 1
    return ans


def compatibility_check(matrix, u, vector):
    extended_matrix = np.concatenate([matrix, vector], axis=1)
    mat_rang = sing_mat_rang(u)
    ext_mat_rang = np.linalg.matrix_rank(extended_matrix)
    return mat_rang == ext_mat_rang


def system_solution2(matrix, vector, p, q, l, u):
    dim = matrix.shape[0]
    if compatibility_check(matrix, u, vector):
        if np.linalg.det(matrix):
            y = np.zeros((dim, 1))
            x = np.zeros((dim, 1))
            bv = p.dot(vector)
            for i in range(dim):
                sum_y = 0
                for k in range(i):
                    sum_y += l[i][k] * y[k]
                y[i] = bv[i] - sum_y
            for j in range(dim):
                sum_x = 0
                for k in range(j):
                    sum_x += u[dim - j - 1][dim - k - 1] * x[dim - k - 1]
                x[dim - j - 1] = (y[dim - j - 1] - sum_x) / u[dim - j - 1][dim - j - 1]
            x = q.dot(x)
        else:
            ma = u
            mpb = np.linalg.inv(l).dot(p).dot(vector)
            x = np.zeros((dim, 1))
            for i in range(dim):
                if np.sum(np.abs(ma[dim-i-1])) + mpb[dim-i-1] != 0:
                    sum_x = 0
                    for k in range(i):
                        sum_x += ma[dim-i-1, dim-k-1]*x[dim-k-1]
                    x[dim-i-1] = (mpb[dim-i-1] - sum_x)/ma[dim-i-1][dim-i-1]
                else:
                    x[dim-i-1] = random.triangular(0, 10)
            x = q.dot(x)
    else:
        x = None
    return x


def singular_matrix_generation():
    matrix = matrix_generation()
    dim = matrix.shape[0]
    row1 = random.randint(1, dim-1)
    alpha = random.randint(0, 10)
    matrix[row1] = alpha*matrix[0]
    return matrix


def diagonally_dominant_mat_generation():
    matrix = matrix_generation()
    dim = matrix.shape[0]
    pos_matrix = np.abs(np.copy(matrix))
    alpha = random.randint(1, 10)
    for i in range(dim):
        matrix[i][i] = alpha*(np.sum(pos_matrix[i]) - pos_matrix[i][i])
    return matrix


def positive_definite_mat_generation():
    dim = random.randint(2, 10)
    matrix = np.random.uniform(0, 10, (dim, dim))
    return np.transpose(matrix).dot(matrix)


def qr_decomposing(matrix):
    dim = matrix.shape[0]
    r = np.zeros((dim, dim))
    q = np.zeros((dim, dim))
    for j in range(dim):
        q[:, j] = np.copy(matrix[:, j])
        for i in range(j):
            r[i, j] = (np.transpose(q[:, i])).dot(q[:, j])
            q[:, j] -= r[i, j]*q[:, i]
        r[j, j] = np.linalg.norm(q[:, j])
        if r[j, j]:
            q[:, j] /= r[j, j]
    return q, r


# Ax = b => QRx = b => x = inv(R)*inv(Q)b = inv(R)*transpose(Q)b
def qr_system_solution(a, b):
    q, r = qr_decomposing(a)
    x = np.linalg.inv(r).dot(np.transpose(q)).dot(b)
    return x


def jacobi(matrix, vector, epsilon):
    matrix_b = -np.linalg.inv(np.diag(np.diag(matrix))).dot(np.tril(matrix) - np.diag(np.diag(matrix))
                                                            + np.triu(matrix) - np.diag(np.diag(matrix)))
    vector_c = np.linalg.inv(np.diag(np.diag(matrix))).dot(vector)
    posterior_est = 0
    a_priori_est = 0
    q = 1
    if np.linalg.norm(matrix_b) < 1:
        a_priori_est += 1 + int((np.log(epsilon) + np.log(1 - np.linalg.norm(matrix_b))
                                 - np.log(np.linalg.norm(vector_c))) / np.log(np.linalg.norm(matrix_b)))
        q = np.linalg.norm(matrix_b) / (1 - np.linalg.norm(matrix_b))
    else:
        a_priori_est = 'Не выполнено условие ||B|| < 1 => оценка не работает'
    dim = matrix.shape[0]
    x = np.zeros((dim, 1))
    x = matrix_b.dot(x) + vector_c
    norm = 1000
    while norm*q > epsilon:
        posterior_est += 1
        next_x = matrix_b.dot(x) + vector_c
        norm = np.linalg.norm(x - next_x)
        if norm > 1000:
            print('Система расходится по методу Якоби')
            return None, None, None
        x = next_x
    return x, a_priori_est, posterior_est


def seidel(matrix, vector, epsilon):
    matrix_b = -np.linalg.inv(np.tril(matrix)).dot(np.triu(matrix, k=1))
    vector_c = np.linalg.inv(np.tril(matrix)).dot(vector)
    posterior_est = 0
    a_priori_est = 0
    q = 1
    if np.linalg.norm(matrix_b) < 1:
        a_priori_est += 1 + int((np.log(epsilon) + np.log(1 - np.linalg.norm(matrix_b))
                                 - np.log(np.linalg.norm(vector_c))) / np.log(np.linalg.norm(matrix_b)))
        q = np.linalg.norm(matrix_b) / (1 - np.linalg.norm(matrix_b))
    else:
        a_priori_est = 'Не выполнено условие ||B|| < 1 => оценка не работает'
    dim = matrix.shape[0]
    x = np.zeros((dim, 1))
    x = matrix_b.dot(x) + vector_c
    norm = 1000
    while norm * q > epsilon:
        posterior_est += 1
        next_x = matrix_b.dot(x) + vector_c
        norm = np.linalg.norm(x - next_x)
        if norm > 1000:
            print('Система расходится по методу Зейделя')
            return None, None, None
        x = next_x
    return x, a_priori_est, posterior_est
