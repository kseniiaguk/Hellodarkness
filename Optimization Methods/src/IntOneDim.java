import java.util.function.DoubleFunction;

public interface IntOneDim {
    public double minimize(double a, double b, double epsilon, DoubleFunction<Double> f);
}