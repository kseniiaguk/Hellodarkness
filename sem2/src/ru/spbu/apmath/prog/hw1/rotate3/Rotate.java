package ru.spbu.apmath.prog.hw1.rotate3;

import java.util.ArrayList;

public class Rotate {
    public ArrayList<Integer> rotate(ArrayList<Integer> input){
        ArrayList<Integer> answer = new ArrayList<>();
        if (input.size() != 0){
            answer.add(0,input.get(input.size()-1));
            for (int i = 1; i < input.size(); i++){
            answer.add(i, input.get(i-1));
            }
            return answer;}
        else{
            return answer;
        }
    }
}
