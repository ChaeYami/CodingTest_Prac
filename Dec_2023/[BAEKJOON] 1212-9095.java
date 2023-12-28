// https://www.acmicpc.net/problem/9095

import java.util.Scanner;

public class Main { 
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        
        for (int i = 0; i<T; i++){
            int n = scanner.nextInt();
            System.out.println(Recur(n));
        }
    }
    private static int Recur(int num){
        if (num == 1) {
            return 1;
        } else if (num == 2) {
            return 2;
        } else if (num == 3) {
            return 4;
        } else {
            return (Recur(num - 3) + Recur(num - 2) + Recur(num - 1));
        }
    }
}
