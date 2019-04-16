import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        System.out.println("Введите количество элементов");
        Scanner scan1 = new Scanner(System.in);
        ArrayList<Integer> myList = new ArrayList<>();
        try {
            int number = scan1.nextInt();
            if (number == 0) {
                Rotate myList1 = new Rotate();
                System.out.println(myList1.rotate(myList));
            } else {
                try {
                    for (int i = 0; i < number; i++) {
                        System.out.println("Введите элемент массива");
                        Scanner scan = new Scanner(System.in);
                        int myInt = scan.nextInt();
                        myList.add(myInt);
                    }
                    Rotate myList1 = new Rotate();
                    System.out.println(myList1.rotate(myList));
                } catch (IndexOutOfBoundsException e2) {
                    System.out.println("Неверный ввод");
                }
            }
        }
        catch (InputMismatchException e){
            System.out.println("Неверный ввод");
        }
    }
}
