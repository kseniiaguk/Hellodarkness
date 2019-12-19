import static java.lang.StrictMath.exp;

public class Dichotomy {
    private double function(double a, double b, double x) {// Заданная функция
        return a * x + b / (exp(x));}
    public double dichotomy(double a, double b) {
        double x;//Середина отрезка
        double l;//Значение слева от центра
        double r;//Значение справа от центра
        double left = -100000;// Левая граница области
        double right = 100000;// Правая граница области
        double delta = 0.0000001;// Допустимая погрешность
        double epsilon = 2 * delta + 0.00000001;//Точность
        int k = 0; // Количество итераций
        while (Math.abs((right - left)) >= epsilon) {
            k++;
            //System.out.print("ШАГ " + k);
            //System.out.println(" отрезок: от " + left + " до " + right);
            x = (left + right) / 2;// Считаем середину отрезка
            //System.out.println("Середина: " + x);
            l = function(a, b, x - delta);// Считаем значение функции в точке слева от центра
            r = function(a, b, x + delta);// Считаем значение функции в точке справа от центра
            //System.out.println("Значение слева: " + l + ", значение справа: " + r);
            if (l < r) {// Для поиска максимума меняем знак на противоположный
                right = x;// Меняем правую границу отрезка
            } else {
                left = x;// Меняем левую границу отрезка
            }
        }

        x = (left + right) / 2;
        System.out.print("При x = " + x);
        return function(a, b, x);

    }
}