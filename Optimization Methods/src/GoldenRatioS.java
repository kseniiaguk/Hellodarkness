import static java.lang.StrictMath.exp;

    public class GoldenRatioS {
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
            return function(a,b,x);
        }
    }
