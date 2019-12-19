/*import static java.lang.StrictMath.exp;

public class GoldenRatio {
    final double phi = (1 + Math.sqrt(5)) / 2;// Пропорция золотого сечения

    final double function(double a, double b, double x) {// Заданная функция
        return a * x + b / (exp(x));}

    double goldenRatio(double a, double b){
        double x;
        double delta = 0.0000001;// Допустимая погрешность
        double epsilon = 2 * delta + 0.00000001;//Точность
        double left = -100000;// Левая граница области
        double right = 100000;// Правая граница области
        double x1, x2;
        int k = 0;// Количество итераций
        while (true){
            k++;
            //System.out.println("ШАГ " + k);
            x1 = right - (right - left) / phi;
            x2 = left + (right - left) / phi;
            //System.out.println("Точки деления: " + x1 + " и " + x2);
            //System.out.println("Значения функции: " + function(a,b,x1)+ " и " + function(a,b,x2));
            if (function(a,b,x1) >= function(a,b,x2))
                left = x1;
            else
                right = x2;
            if (Math.abs(right - left) < epsilon)
                break;
        }
        x = (left + right) / 2;
        System.out.print("При x = " + x);
        return x;
    }
}*/

import java.util.function.DoubleFunction;

import static java.lang.Math.exp;

public class GoldenRatio implements IntOneDim{
    final double function(double a, double b, double x) {// Заданная функция
        return a * x + b / (exp(x));}
    private final double PHI = (1 + Math.sqrt(5)) / 2;
    public GoldenRatio() {
    }

    @Override
    public double minimize(double a, double b, double epsilon, DoubleFunction<Double> f){
        double x1, x2;
        while (true){
            if (Math.abs(b - a) < epsilon)
                break;
            x1 = b - (b - a) / PHI;
            x2 = a + (b - a) / PHI;
            if (f.apply(x1) >= f.apply(x2))
                a = x1;
            else
                b = x2;
        }
        double x = (a + b) / 2;
        double m = function(a,b,x);
        return (a + b) / 2;
    }
}