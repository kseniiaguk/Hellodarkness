package ru.spbu.apmath.prog.hw1.rotate3;

import java.util.ArrayList;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String myStr = scan.nextLine();
        ArrayList myList = new ArrayList();
        for (int i = 0; i < myStr.length(); i++) {
            myList.add(myStr.charAt(i));
        }
        Rotate myList1 = new Rotate();
        System.out.println(myList1.rotate(myList));
    }
}