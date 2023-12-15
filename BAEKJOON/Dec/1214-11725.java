import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.Queue;

/*
public class Main {
    static int N;
    static ArrayList<Integer>[] graph;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        graph = new ArrayList[N + 1];
        visited = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 1; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        dfs(1);

        for (int x = 2; x <= N; x++) {
            System.out.println(visited[x]);
        }
    }

    static void dfs(int node) {
        Stack<Integer> stack = new Stack<>();
        stack.push(node);

        while (!stack.isEmpty()) {
            int top = stack.pop();

            for (int adj : graph[top]) {
                if (visited[adj] == 0) {
                    visited[adj] = top;
                    stack.push(adj);
                }
            }
        }
    }
}
 */

public class Main {
    static int N;
    static ArrayList<Integer>[] graph;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        graph = new ArrayList[N+1];
        visited = new int[N+1];

        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 1; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }
        bfs(1);

        for (int x = 2; x <= N; x++) {
            System.out.println(visited[x]);
        }
    }

    static void bfs(int start){
        Queue<Integer> deq = new ArrayDeque<>();
        deq.offer(start);

        while (!deq.isEmpty()) {
            int node = deq.poll();

            for (int adj : graph[node]) {
                if (visited[adj] == 0) {
                    visited[adj] = node;
                    deq.offer(adj);
                }
            }
        }
    }
}
