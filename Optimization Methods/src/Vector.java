import java.util.function.BiFunction;


public class Vector {
    private double x, y;

    public Vector(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public Vector(Vector point) {
        this.x = point.getX();
        this.y = point.getY();
    }
    public double getX() {
        return this.x;
    }

    public double getY() {
        return this.y;
    }

    public Vector subtraction(Vector b) {
        return new Vector(x - b.getX(), y - b.getY());
    }

    public Vector sum(Vector b) {
        return new Vector(x + b.getX(), y + b.getY());
    }

    public Vector multiply(double s) {
        return new Vector(x * s, y * s);
    }

    public static Vector getGradient(BiFunction<Double, Double, Double> f, Vector point, double epsilon) {
        double dfx = (f.apply(point.getX() + epsilon, point.getY()) - f.apply(point.getX(), point.getY())) / epsilon;
        double dfy = (f.apply(point.getX(), point.getY() + epsilon) - f.apply(point.getX(), point.getY())) / epsilon;
        return new Vector(dfx, dfy);
    }

    public double skal(Vector b) {
        return x * b.getX() + y * b.getY();
    }

    public double getNorm() {
        return Math.sqrt((x * x) + (y * y));
    }

    public Matrix pointMultiply(Vector a) {
        return new Matrix(this.x * a.getX(), this.y * a.getX(), this.x * a.getY(), this.y * a.getY());
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public Matrix columnTimesRow(Vector point) {
        return new Matrix(this.x * point.getX(), this.y * point.getX(), this.x * point.getY(), this.y * point.getY());
    }

    public void show() {
        System.out.println(getX() + "   " + getY());
    }
}
