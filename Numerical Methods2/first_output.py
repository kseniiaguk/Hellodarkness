from first import *

# ПРОВЕРКИ
# ---------------------------------------------------------
# Задание 1-------------------------------------------------
matrix_a = matrix_generation()
mat_dim = matrix_a.shape[0]
s, p1, q1, l, u = lu_decomposing(matrix_a)
p = p_matrix_formation(p1)
q = q_matrix_formation(q1)
b = b_generation(mat_dim)
det_matrix = upper_triangle_determinant(u, s)
inv_matrix = inverse_matrix(matrix_a, l, u, p)
cond_number = (np.linalg.norm(inverse_matrix(matrix_a, l, u, p))*np.linalg.norm(matrix_a))
x = system_solution(l, u, b, p)
print('-----Задание 1: LU-разложение-----\n')
print('Матрица A:\n', matrix_a)
print('Результаты разложения.\nМатрица L:\n', l)
print('Матрица U:\n', u)
print('Матрица P:\n', p)
print('Матрица Q:\n', q)
print('Проверим правильность разложения. Матрица PA:\n', p.dot(matrix_a))
print('Матрица LU:\n', l.dot(u))
print('a) Определитель матрицы A:\n', det_matrix)
print('Проверим с помощью встроенной функции:\n', np.linalg.det(matrix_a))
print('b) Решение СЛАУ. Вектор b:\n', b)
print('Решение x:\n', x)
print('Проверим правильность. Ax:\n', matrix_a.dot(x))
print('c) Обратная матрица. A^(-1):\n', inv_matrix)
print('Проверим: A*A^(-1)=\n', np.abs(np.around(matrix_a.dot(inv_matrix))))    # Приходится округлять и брать модуль
# из-за формата дробных чисел в python. Вывод результата без округления и взятия модуля закомментирован исключительно
# ради красоты.
# print('Проверим: A*A^(-1)=\n', matrix_a.dot(inv_matrix))
print('d) Число обусловленности равно ', cond_number)
# Задание 2-------------------------------------------------
print('-----Задание 2: LU-разложение для случая с вырожденной матрицей-----\n')
singular_matrix = singular_matrix_generation()
dim2 = singular_matrix.shape[0]
s2, p22, q22, l2, u2 = full_pivot_lu_dec(singular_matrix)
p2 = p_matrix_formation(p22)
q2 = q_matrix_formation(q22)
b2 = b_generation(dim2)
sing_mat_sample = np.array([[1.0, 1.0, 1.0], [2.0, 2.0, 2.0], [3.0, 2.0, 1.0]])
vector_sample = np.array([[1.0], [2.0], [1.0]])
ss, ps1, qs1, ls, us = full_pivot_lu_dec(sing_mat_sample)
ps = p_matrix_formation(ps1)
qs = q_matrix_formation(qs1)
print('Матрица A:\n', singular_matrix)
print('Результаты разложения.\nМатрица L:\n', l2)
print('Матрица U:\n', u2)
print('Матрица P:\n', p2)
print('Матрица Q:\n', q2)
print('Проверим правильность разложения. Матрица PAQ:\n', p2.dot(singular_matrix).dot(q2))
print('Матрица LU:\n', l2.dot(u2))
print('Ранг матрицы A:\n', sing_mat_rang(u2))
print('Решение СЛАУ. Вектор b:\n', b2)
if system_solution2(singular_matrix, b2, p2, q2, l2, u2) is not None:
    print('Частное решение: x=\n', system_solution2(singular_matrix, b2, p2, q2, l2, u2))
    print('Ax:\n', singular_matrix.dot(system_solution2(singular_matrix, b2, p2, q2, l2, u2)))
else:
    print("Система несовместна")
print('Проверим правильность работы программы с помощью заготовленной системы, имеющией бесконечное множество решений'
      '. Матрица A1:\n', sing_mat_sample)
print('Вектор b1:\n', vector_sample)
if system_solution2(sing_mat_sample, vector_sample, ps, qs, ls, us) is not None:
    print('Частное решение:\n', system_solution2(sing_mat_sample, vector_sample, ps, qs, ls, us))
    print('Ax:\n', sing_mat_sample.dot(system_solution2(sing_mat_sample, vector_sample, ps, qs, ls, us)))
else:
    print("Система несовместна")
# Задание 3-------------------------------------------------
print('-----Задание 3: QR-разложение-----\n')
q, r = qr_decomposing(matrix_a)
x1 = qr_system_solution(matrix_a, b)
print('Результаты разложения.\nМатрица Q:\n', q)
print('Матрица R:\n', r)
print('Проверим правильность разложения. Матрица A:\n', matrix_a)
print('Матрица QR:\n', q.dot(r))
print('Решение СЛАУ. Вектор b:\n', b)
print('Решение x:\n', x1)
print('Проверим правильность. Ax:\n', matrix_a.dot(x1))
# Задание 4-------------------------------------------------
print('-----Задание 4: Методы Якоби и Зейделя-----\n')
positive_mat = positive_definite_mat_generation()
diag_dom_mat = diagonally_dominant_mat_generation()
pos_dim = positive_mat.shape[0]
diag_dim = diag_dom_mat.shape[0]
pos_vector = b_generation(pos_dim)
diag_vector = b_generation(diag_dim)
accuracy = 1.e-10
print('Метод Якоби\n')
print('1) Для положительно определённой матрицы.\n Матрица A:\n', positive_mat)
print('Вектор b:\n', pos_vector)
print('Результаты.\n')
if jacobi(positive_mat, pos_vector, accuracy)[0] is not None:
    print('Априорная оценка:\n', jacobi(positive_mat, pos_vector, accuracy)[1])
    print('Апостериорная оценка:\n', jacobi(positive_mat, pos_vector, accuracy)[2])
    print('Решение:\n', jacobi(positive_mat, pos_vector, accuracy)[0])
    print('Проверим правильность с помощью встроенной функции:\n', np.linalg.solve(positive_mat, pos_vector))
print('2) Для матрицы с диагональным преобладанием.\n Матрица A:\n', diag_dom_mat)
print('Вектор b:\n', diag_vector)
print('Результаты.\n')
if jacobi(diag_dom_mat, diag_vector, accuracy)[0] is not None:
    print('Априорная оценка:\n', jacobi(diag_dom_mat, diag_vector, accuracy)[1])
    print('Апостериорная оценка:\n', jacobi(diag_dom_mat, diag_vector, accuracy)[2])
    print('Решение:\n', jacobi(diag_dom_mat, diag_vector, accuracy)[0])
    print('Проверим правильность с помощью встроенной функции:\n', np.linalg.solve(diag_dom_mat, diag_vector))
print('Метод Зейделя\n')
print('1) Для положительно определённой матрицы.\n Матрица A:\n', positive_mat)
print('Вектор b:\n', pos_vector)
print('Результаты.\n')
if seidel(positive_mat, pos_vector, accuracy)[0] is not None:
    print('Априорная оценка:\n', seidel(positive_mat, pos_vector, accuracy)[1])
    print('Апостериорная оценка:\n', seidel(positive_mat, pos_vector, accuracy)[2])
    print('Решение:\n', seidel(positive_mat, pos_vector, accuracy)[0])
    print('Проверим правильность с помощью встроенной функции:\n', np.linalg.solve(positive_mat, pos_vector))
print('2) Для матрицы с диагональным преобладанием.\n Матрица A:\n', diag_dom_mat)
print('Вектор b:\n', diag_vector)
print('Результаты.\n')
if seidel(diag_dom_mat, diag_vector, accuracy)[0] is not None:
    print('Априорная оценка:\n', seidel(diag_dom_mat, diag_vector, accuracy)[1])
    print('Апостериорная оценка:\n', seidel(diag_dom_mat, diag_vector, accuracy)[2])
    print('Решение:\n', seidel(diag_dom_mat, diag_vector, accuracy)[0])
    print('Проверим правильность с помощью встроенной функции:\n', np.linalg.solve(diag_dom_mat, diag_vector))