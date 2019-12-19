import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        Dichotomy dichotomy = new Dichotomy();
        GoldenRatioS goldenRatio = new GoldenRatioS();

        double a = 0;
        double b = 0;
        // ввод параметров
        System.out.println("Введите параметр a");
        try {
            a = scanner.nextDouble();
        } catch (Exception e) {
            throw new IOException();
        }
        System.out.println("Введите параметр b");
        try {
            b = scanner.nextDouble();
        } catch (Exception e) {
            throw new IOException();
        }

        System.out.println("--------------ОДНОМЕРНАЯ--ОПТИМИЗАЦИЯ---------------------");
        System.out.println("1) ДИХОТОМИЯ:");
        System.out.println(" функция f(x) = " + a + "*x + " + b + "/(e^x) " + "достигает  минимума "
                + dichotomy.dichotomy(a, b));
        System.out.println("2) ЗОЛОТОЕ СЕЧЕНИЕ:");
        System.out.println(" функция f(x) = " + a + "*x + " + b + "/(e^x) " + "достигает  минимума "
                + goldenRatio.goldenRatio(a, b));

    }
}