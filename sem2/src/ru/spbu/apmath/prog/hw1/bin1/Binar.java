package ru.spbu.apmath.prog.hw1.bin1;


public class Binar {
    public int num;
    public Binar(int num){
        this.num = num;
    }
    public String ans = "";
    public String toBin(){
        int deg = 0;
        int myNum = num;
        if (myNum != 0) {
            if (myNum < 0){
                ans += "-";
                myNum = -myNum;
            }
            int div = myNum;
            while (myNum >= 1) {
                myNum /= 2;
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
        else {
            ans = "0";
        }
        return ans;
    }
}
