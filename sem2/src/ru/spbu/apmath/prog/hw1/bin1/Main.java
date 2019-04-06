package ru.spbu.apmath.prog.hw1.bin1;

import java.util.Scanner;
public class Main {
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Введите целое десятичное число");
        String input = scan.nextLine();
        try {
            int numb = Integer.parseInt(input);
            Binar yourNumber = new Binar(numb);
            System.out.println("В двоичной системе счисления: " + yourNumber.bin());
        }
        catch (IllegalArgumentException e){
            System.out.println("Неверный ввод");
        }
    }
}
