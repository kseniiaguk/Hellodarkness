from math import sqrt

# Задаём функции для дальнейшей оптимизации
def rosenbrock(x, y):
    return 5 * (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def himmelblau(x, y):
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2

# Градиент
def gradient(f):
    delta = 8e-15
    x_deriv = lambda x, y: (f(x + delta, y) - f(x, y)) / delta
    y_deriv = lambda x, y: (f(x, y + delta) - f(x, y)) / delta
    return lambda x, y: (x_deriv(x, y), y_deriv(x, y))

# Модуль вектора
def vector_module(x, y):
    return sqrt(x ** 2 + y ** 2)

# Умножение вектора на число
def scalar_mul(x_1, y_1, x_2, y_2):
    return x_1 * x_2 + y_1 * y_2

# Золотое сечение
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


def optimize(f, x_0, y_0, eps): # Здесь f - функция, которую минимизируем, x_0, y_0, - координаты точки, eps - точность
    grad = gradient(f)
    x_direction, y_direction = grad(x_0, y_0) # Считаем градиент в заданной точке
    x_direction, y_direction = -x_direction, -y_direction # Задаём антиградиентное направление

    counter = 0 # Счётчик итераций
    while vector_module(*grad(x_0, y_0)) != 0:
        counter += 1

        single_arg_func = lambda alpha: f(x_0 + alpha * x_direction, y_0 + alpha * y_direction)
        alpha = golden_ratio(single_arg_func, 0, 100, eps) # С помощью Золотого сечения высчитываем коэффициент

        old_x_0 = x_0
        old_y_0 = y_0
        x_0 += alpha * x_direction
        y_0 += alpha * y_direction

        new_x_direction, new_y_direction = grad(x_0, y_0)
        new_x_direction, new_y_direction = -new_x_direction, -new_y_direction
        old_grad_module = vector_module(x_direction, y_direction) ** 2
        new_grad_module = scalar_mul(new_x_direction, new_y_direction, x_direction, y_direction)
        beta = new_grad_module / old_grad_module
        old_x_direction = x_direction
        old_y_direction = y_direction
        x_direction = new_x_direction + beta * x_direction
        y_direction = new_y_direction + beta * y_direction

        cond_1 = vector_module(x_0 - old_x_0, y_0 - old_y_0)
        cond_2 = vector_module(x_direction, y_direction)
        if (min(cond_1, cond_2) < eps):
            break

    return ([x_0, y_0], f(x_0, y_0), counter)


def main():
    print("МЕТОД СОПРЯЖЁННЫХ ГРАДИЕНТОВ:")
    # print("---Розенброк-------------------------------------")
   # print("Функция 100(y-x^2)^2+5(1-x)^2 достигает в точке ", optimize(rosenbrock, -1, 1.5, 1e-10)[0], " минимума ",
    #      optimize(rosenbrock, -1, 1.5, 1e-10)[1], ", кол-во итераций: ", optimize(rosenbrock, -1, 1.5, 1e-10)[2])  # 1,0
    print("---Химмельблау-------------------------------------")
    print("Функция (x^2+y-11)^2+(x+y^2-7)^2 достигает в точке ", optimize(himmelblau, 0, 0, 1e-10)[0], " минимума ",
          optimize(himmelblau, 0, 0, 1e-10)[1], ", кол-во итераций: ", optimize(himmelblau, 0, 0, 1e-10)[2])


if __name__ == "__main__":
    main()