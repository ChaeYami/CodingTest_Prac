/* https://www.acmicpc.net/problem/2775 */

import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();

        for (int t = 0; t<T; t++){
            int k = scanner.nextInt();
            int n = scanner.nextInt();

            // 1행, n+1열(0층부터 시작하므로) 크기의 이차원 배열 생성 
            int[][] floor = new int[1][n + 1];

            // 0층 업데이트
            for (int i = 1; i <= n; i++) {
                floor[0][i] = i;

            }

            // 그 위의 층
            for (int i = 1; i<=k; i++){
                // 1호는 어차피 1명이므로 2호부터 시작
                for (int j = 2; j<=n; j++){
                    floor[0][j] = floor[0][j-1] + floor[0][j];
                }
            }
            System.out.println(floor[0][n]);
        }
        scanner.close();
    }
}



