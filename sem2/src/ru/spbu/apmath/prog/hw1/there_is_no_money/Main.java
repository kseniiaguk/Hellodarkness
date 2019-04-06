package ru.spbu.apmath.prog.hw1.there_is_no_money;

import java.util.Scanner;
public class Main {
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Введите количество сотрудников");
        try {
        int input = scan.nextInt();
        String[] nameArray = new String[input];
        Double[] hSalaryArray = new Double[input];
        String[] SalaryArray = new String[input];
            for (int i = 0; i < input; i++){
                System.out.println("Введите поочерёдно (через enter) имя, зрпл/час и часы работы сотрудника");
                Scanner scan1 = new Scanner(System.in);
                String name = scan1.nextLine();
                double hourSalary = scan1.nextDouble();
                int time = scan1.nextInt();
                Employee employer = new Employee(name, hourSalary, time);
                nameArray[i] = (employer.name);
                hSalaryArray[i] = (employer.hourSalary);
                try {
                    SalaryArray[i] = (String.valueOf(employer.getSalary()));
                }
                catch (IllegalArgumentException e1){
                    SalaryArray[i] = "Ошибка";
                }
            }
        for (int i = 0; i < input; i++){
            System.out.println(nameArray[i] + " " + hSalaryArray[i] + " " + SalaryArray[i]);
        }
        }
        catch (java.util.InputMismatchException e){
            System.out.println("Неверный ввод");
        }
    }
}
