package ru.spbu.apmath.prog.hw1.there_is_no_money;

public class Employee {
    public String name;
    public double hourSalary;
    public int time;
    public Employee(String name, Double hourSalary, int time){
        this.name = name;
        this.hourSalary = hourSalary;
        this.time = time;
    }
    public double getSalary(){
        if ((hourSalary >= 70)&(time <= 60)){
            double salary = 0;
            if (time > 40) {
                int over = time - 40;
                salary += 40 * hourSalary + 1.5 * over * hourSalary;
            } else {
                salary += hourSalary * time;
            }
            return salary;
        }
        else{
            throw new IllegalArgumentException ("Недопустимые данные");
        }
    }
}
