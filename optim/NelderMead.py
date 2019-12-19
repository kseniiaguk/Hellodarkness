from math import sqrt


alpha = 1
beta = 2
gamma = 0.5


def rosenbrock(x, y):
    return 5 * (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def himmelblau(x, y):
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2


def point_distance(x_1, y_1, x_2, y_2):
    return sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)


def optimize(f, x_0, y_0, eps):
    size = 2
    f_0 = f(x_0, y_0)

    x_1 = x_0 + size
    y_1 = y_0
    f_1 = f(x_1, y_1)

    x_2 = size / 2
    y_2 = y_0 + sqrt(3) * size / 2
    f_2 = f(x_2, y_2)

    vertexes = [(x_0, y_0, f_0), (x_1, y_1, f_1), (x_2, y_2, f_2)]

    center_x = (vertexes[0][0] + vertexes[1][0] + vertexes[2][0]) / 3
    center_y = (vertexes[0][1] + vertexes[1][1] + vertexes[2][1]) / 3
    dist_1 = point_distance(center_x, center_y, vertexes[0][0], vertexes[0][1])
    dist_2 = point_distance(center_x, center_y, vertexes[1][0], vertexes[1][1])
    dist_3 = point_distance(center_x, center_y, vertexes[2][0], vertexes[2][1])
    distance = max(dist_1, dist_2, dist_3)

    counter = 0
    while distance > eps:
        counter += 1

        vertexes = sorted(vertexes, key = lambda x : x[2], reverse = True)
        max_x, max_y, max_f = vertexes[0]
        vertexes = vertexes[1:]
        middle_x = (vertexes[0][0] + vertexes[1][0]) / 2
        middle_y = (vertexes[0][1] + vertexes[1][1]) / 2

        mirror_x = middle_x + alpha * (middle_x - max_x)
        mirror_y = middle_y + alpha * (middle_y - max_y)
        mirror_f = f(middle_x, middle_y)

        if mirror_f < max_f:
            if mirror_f > vertexes[1][2]:
                vertexes.append((mirror_x, mirror_y, mirror_f))
            else:
                far_x = middle_x + beta * (mirror_x - middle_x)
                far_y = middle_y + beta * (mirror_y - middle_y)
                far_f = f(far_x, far_y)
                if far_f < mirror_f:
                    vertexes.append((far_x, far_y, far_f))
                else:
                    vertexes.append((mirror_x, mirror_y, mirror_f))
        else:
            near_x, near_y = 0, 0
            if mirror_f > max_f:
                near_x = middle_x - gamma * (max_x - middle_x)
                near_y = middle_y - gamma * (max_y - middle_y)
            else:
                near_x = middle_x - gamma * (mirror_x - middle_x)
                near_y = middle_y - gamma * (mirror_y - middle_y)
            near_f = f(near_x, near_y)
            vertexes.append((near_x, near_y, near_f))
            if near_f >= max_f:
                min_x, min_y, min_f = vertexes[1]
                new_vertexes = []
                for old_x, old_y, old_f in vertexes:
                    new_x = (old_x + min_x) / 2
                    new_y = (old_y + min_y) / 2
                    new_f = f(new_x, new_y)
                    new_vertexes.append((new_x, new_y, new_f))
                vertexes = new_vertexes
        center_x = (vertexes[0][0] + vertexes[1][0] + vertexes[2][0]) / 3
        center_y = (vertexes[0][1] + vertexes[1][1] + vertexes[2][1]) / 3
        dist_1 = point_distance(center_x, center_y, vertexes[0][0], vertexes[0][1])
        dist_2 = point_distance(center_x, center_y, vertexes[1][0], vertexes[1][1])
        dist_3 = point_distance(center_x, center_y, vertexes[2][0], vertexes[2][1])
        distance = max(dist_1, dist_2, dist_3)

    return ([center_x, center_y], f(center_x, center_y), counter)


def main():
    print("МЕТОД НЕЛДЕРА-МИДА:")
    # print("---Розенброк-------------------------------------")
    #print("Функция 100(y-x^2)^2+5(1-x)^2 достигает в точке ", optimize(rosenbrock, -2, 2, 1e-8)[0], "минимума",
     #     optimize(rosenbrock, -2, 2, 1e-8)[1], ", кол-во итераций: ", optimize(rosenbrock, -2, 2, 1e-8)[2])
    print("---Химмельблау-------------------------------------")
    print("Функция (x^2+y-11)^2+(x+y^2-7)^2 достигает в точке ", optimize(himmelblau, 0, 0, 1e-8)[0], "минимума",
          optimize(himmelblau, 0, 0, 1e-8)[1], ", кол-во итераций:", optimize(himmelblau, 0, 0, 1e-8)[2])


if __name__ == "__main__":
    main()