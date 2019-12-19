/*public class Gradient {
    private static double func(double[] point){//Заданная функция
        double x1 = point[0];
        double x2 = point[1];
        return 100 * Math.pow((x2 - Math.pow(x1,2)), 2) + 5 * Math.pow((1 - x1), 2);
    }
    /*private static double func(double[] point){
        double x1 = point[0];
        double x2 = point[1];
        return Math.pow((Math.pow(x1, 2)) + x2 - 11, 2) + Math.pow((x1 + Math.pow(x2, 2) - 7), 2);
    }
    public static double gradient() {
        String point_min;
        Vector v1 =  new Vector(0.0,0.0);// Исходная точка
        double alpha = v1.dichotomy();// размер шага
        Vector v2 = v1.getNextVector(alpha);
        int k = 0;
        while (v1.distance(v2) > v1.eps){
            k++;
            //System.out.println(v1.distance(v2));
            //System.out.println(alpha);

            System.out.println(f_v1);
            System.out.println(f_v2);
            //System.out.println(v2.grad().repr() +" "+ v1.grad().repr());
            v1 = v2;
            alpha = v1.dichotomy();
            v2 = v1.getNextVector(alpha);}
        point_min = v1.repr();
        System.out.print("В точке " + point_min);
        return 4 - func(v1.c());
    }
}*/
import java.util.function.BiFunction;

public class Gradient implements IntTwoDim {
    private double epsilon;
    private Vector x0;
    private BiFunction<Double, Double, Double> f;
    private BiFunction<Double, Double, Double> df = (dfx, dfy) -> dfx + dfy;


    public Gradient(BiFunction<Double, Double, Double> f, Vector startPoint, double epsilon) {
        this.epsilon = epsilon;
        this.f = f;
        this.x0 = startPoint;
    }

    @Override
    public double[] minimize() {
        Vector nextPoint;
        GoldenRatio gd = new GoldenRatio();
        int iter = 0;
        while (true) {
            Vector grad = Vector.getGradient(f, x0, epsilon);
            final Vector finalStartPoint = x0;
            double stepSize = gd.minimize(0.0, 1.0, 1e-05,
                    (x) -> {
                        Vector point = finalStartPoint.subtraction(grad.multiply(x));
                        return f.apply(point.getX(), point.getY());
                    });


            nextPoint = x0.subtraction(grad.multiply(stepSize));
//            System.out.println("Точка : " + x0.getX() + "   " +  x0.getY());
            iter++;
            Boolean stopCriteria1 = nextPoint.subtraction(x0).getNorm() < epsilon;
            Boolean stopCriteria2 = Math.abs(f.apply(nextPoint.getX(), nextPoint.getY()) - f.apply(x0.getX(), x0.getY())) < epsilon;
            if (stopCriteria1 || stopCriteria2) {
//                System.out.println("Количество итераций: " + iter);
                return new double[]{nextPoint.getX(), nextPoint.getY()};
            }

            x0 = new Vector(nextPoint.getX(), nextPoint.getY());


        }


    }


}

