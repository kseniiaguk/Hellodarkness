package ru.spbu.apmath.prog.hw1.bin1;


public class Binar {
    public int num;
    public Binar(int num){
        this.num = num;
    }
    public String ans = "";
    public String bin(){
        int deg = 0;
        if (num > 0) {
            int div = num;
            while (num >= 1) {
                num /= 2;
                deg++;
            }
            for (int i = deg - 1; i >= 0; i--) {
                if (div >= Math.pow(2, i)) {
                    ans += "1";
                    div -= Math.pow(2, i);
                } else {
                    ans += "0";
                }
                deg--;
            }
        }
        else if (num == 0){
            ans = "0";
        }
        else {
            int num1 = -num;
            int div = num1;
            while (num1 >= 1) {
                num1 /= 2;
                deg++;
            }
            ans += "-";
            for (int i = deg - 1; i >= 0; i--) {
                if (div >= Math.pow(2, i)) {
                    ans += "1";
                    div -= Math.pow(2, i);
                } else {
                    ans += "0";
                }
                deg--;
            }
        }
        return ans;
    }
}

