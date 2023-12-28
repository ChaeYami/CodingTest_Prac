import java.io.BufferedReader;
import java.io.EOFException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;


public class Main{
    static int comNum;
    static int pairNum;
    static boolean[] visited;
    static ArrayList<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        StringBuilder answer = new StringBuilder();
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        // 입력값 받아오기
        comNum = Integer.parseInt(reader.readLine()); // 컴퓨터수
        pairNum = Integer.parseInt(reader.readLine()); // 쌍의 수
        graph = new ArrayList[comNum+1]; //0번 인덱스는 안 쓰므로 +1
        visited = new boolean[comNum +1];
        // 그래프 리스트 생성
        for (int i = 1 ; i<=comNum; i++){
            graph[i] = new ArrayList<>();
        }
        // 입력받은 쌍으로 그래프 리스트 값 삽입
        for (int i =1; i<=pairNum;i++){
            StringTokenizer pair = new StringTokenizer(reader.readLine());
            int first = Integer.parseInt(pair.nextToken());
            int second = Integer.parseInt(pair.nextToken());
            graph[first].add(second);
            graph[second].add(first);
        }
        // DFS를 수행할 스택 생성 (방문해야 할 노드의 목록)
        Stack<Integer> stack = new Stack<>();
        stack.push(1); // 1번 컴퓨터가 바이러스
        visited[1] = true;
        int count = 0;
        // 스택이 비지 않는 동안 반복
        while(! stack.isEmpty()){
            int currentNode = stack.pop();
//            answer.append(currentNode);
            for (int nextNode : graph[currentNode]) {
                if (!visited[nextNode]) {
                    visited[nextNode] = true;
                    count ++;
                    stack.push(nextNode);
                }
            }
        }
        answer.append(count);
        System.out.println(answer);
    }


}