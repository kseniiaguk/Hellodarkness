import java.util.function.BiFunction;

public class MainGrad {
    private static double func1(double[] point){
        double x1 = point[0];
        double x2 = point[1];
        return 100 * Math.pow((x2 - Math.pow(x1,2)), 2) + 5 * Math.pow((1 - x1), 2);}
    private static double func2(double[] point){
        double x1 = point[0];
        double x2 = point[1];
        return Math.pow((x2 + Math.pow(x1,2) - 11), 2) + Math.pow((x1 + Math.pow(x2,2) - 7), 2);}
    public static void main(String[] args){
        BiFunction<Double, Double, Double> rosenbrock = (x1, x2) -> 100 * Math.pow(x2 - x1 * x1, 2) + 5 * Math.pow(1 - x1, 2);
        BiFunction<Double, Double, Double> himmelblau = (x1, x2) -> Math.pow(Math.pow(x1, 2) + x2 - 11, 2) + Math.pow(x1 + Math.pow(x2, 2) - 7, 2);
        Gradient gd1 = new Gradient(rosenbrock, new Vector(-1, 0), 1e-4);
        Gradient gd2 = new Gradient(himmelblau, new Vector(0, 0), 1e-4);
        double[] result1 = gd1.minimize();
        double[] result2 = gd2.minimize();
        System.out.println("-----------------------------------ДВУМЕРНЫЕ--------------------------------");
        System.out.println("ГРАДИЕНТНЫЙ МЕТОД:");
        System.out.println("---Розенброка--------------------:");
        System.out.println("При х = " + result1[0] + " и у = " + result1[1] + " функция достигает минимума " + func1(new double[] {result1[0],result1[1]}));
        System.out.println("---Химмельблау--------------------:");
        System.out.println("При х = " + result2[0] + " и у = " + result2[1] + " функция достигает минимума " + func2(new double[] {result2[0],result2[1]}));
    }
}
