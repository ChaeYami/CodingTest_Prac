import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class main{
    static int mapSize;
    static int [][] complex;
    static int [] dy = {1, -1, 0, 0};
    static int [] dx = {0, 0, 1, -1};
    static int cnt = 0;
    static int complexNum = 0;
    static boolean[][] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();
        List<Integer> houseNum = new ArrayList<>();

        // 지도의 크기 N 받아오기
        mapSize = Integer.parseInt(reader.readLine());
        complex = new int[mapSize][mapSize];
        visited = new boolean[mapSize][mapSize];

        // 입력값(단지 배열) 2차원 배열로 만들기
        for (int i = 0; i < mapSize; i++) {
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            for (int j = 0; j < mapSize; j++) {
                complex[i][j] = Integer.parseInt(tokenizer.nextToken());
            }
        }



        for (int rows = 0; rows < mapSize; rows++) {
            for (int cols = 0; cols < mapSize; cols++) {
                if(visited[rows][cols] == false && complex[rows][cols] == 1){
                    cnt = 0;
                    complexNum++;
                    dfs(rows,cols);
                    houseNum.add(cnt);

                }

            }
        }
    }
    public static void dfs(int x, int y){
        visited[x][y] = true;

        for (int i = 0 ; i < 4 ; i ++){
            int nx = x + dx[i];
            int ny = y + dy[i];


        }
    }

}