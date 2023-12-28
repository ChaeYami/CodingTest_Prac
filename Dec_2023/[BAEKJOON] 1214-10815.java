import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();

        int N = Integer.parseInt(reader.readLine());
        Map<String, Integer> cards = new HashMap<>();

        // 상근이가 가진 카드 리스트
        StringTokenizer input_1 = new StringTokenizer(reader.readLine());
        for(int i=0; i<N; i++){
            cards.put(input_1.nextToken(),i); // 해시맵 자료구조로, 카드를 키, 값에는 아무거나
        }

        int M = Integer.parseInt(reader.readLine());

        // 가지고 있는지 확인할 숫자 리스트,input_2.nextToken() 으로 돌릴거임
        StringTokenizer input_2 = new StringTokenizer(reader.readLine());
        int[] check = new int[M];
        for(int i=0 ; i<M ; i++){
            if (cards.containsKey((input_2.nextToken()))){
                answer.append("1 ");
            } else{
                answer.append("0 ");
            }
        }
        System.out.println(answer);
    }
}