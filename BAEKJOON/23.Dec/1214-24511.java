// ※ 주어진 입력값을 무작정 다 받으려고 하지 말고 넣을 필요가 있는지에 대해서 생각
// ※ queue : x_n의 값이 계속해서 변경 <-> stack : x_n = x_n-1
// ※ 따라서 0일 경우 queue에 추가할 상황 + queue 및 stack에서 삭제할 상황 => deque
// ※ 또한, 인덱스 0 or 1에 대해서 한 번 더 생각하고 사용할 것

/*
 * x_0 = 2
 * (1) q -> FIFO -> x_1 = 1
 * (2) s -> LIFO -> x_2 = 1
 * (3) s -> LIFO -> x_3 = 1
 * (4) q -> FIFO -> x_4 = 4
 */
/*
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 1. 입력 변수 초기화
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
        StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");

        StringBuilder sb = new StringBuilder();

        Deque<Integer> deque = new ArrayDeque<>();

        // 2. 수열 A
        for (int i = 0; i < n; i++) {
            int queueStack = Integer.parseInt(st1.nextToken());
            int element = Integer.parseInt(st2.nextToken());

            if (queueStack == 0) {
                // Q. (예제 1 기준) 왜 이 곳에다가 element를 초기화한 후 deque에 추가하면 4가 아닌 2가 저장될까요?
                deque.addFirst(element);
            }
        }

        // 3. 수열 B
        int m = Integer.parseInt(br.readLine());
        ArrayList<Integer> arrayList = new ArrayList<>();
        st1 = new StringTokenizer(br.readLine(), " ");

        for (int i = 0; i < m; i++) {
            arrayList.add(Integer.parseInt(st1.nextToken()));
        }

        // 4. 로직
        for (int i = 0; i < m; i++) {
            // ※ 어차피 queue에만 값이 있으므로, 뒤(= 데크에서는 앞)에 값을 넣고 맨 앞(= 맨 뒤)의 값을 삭제 ?
            deque.addLast(arrayList.get(i));
            sb.append(deque.pollFirst()).append(" ");
        }

        // 4. 출력
        System.out.println(sb);
        br.close();
    }
}
*/
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        // 1. 입력값 받아오기
        int N = Integer.parseInt(reader.readLine());

        int[] listQueuestack = new int[N];
        int[] currentList = new int[N];

        StringBuilder answer = new StringBuilder();
        // 1번 리스트 - 자료구조의 형태
        StringTokenizer input1 = new StringTokenizer(reader.readLine());
        for (int i = 0; i < N; i++) {
            listQueuestack[i] = Integer.parseInt(input1.nextToken());
        }
        // 2번 리스트 - 자료구조의 요소
        StringTokenizer input2 = new StringTokenizer(reader.readLine());
        for (int i = 0; i < N; i++) {
            currentList[i] = Integer.parseInt(input2.nextToken());
        }

        int M = Integer.parseInt(reader.readLine());
        int[] insertList = new int[M];
        // 3번 리스트 - 입력값 리스트
        StringTokenizer st3 = new StringTokenizer(reader.readLine());
        for (int i = 0; i < M; i++) {
            insertList[i] = Integer.parseInt(st3.nextToken());
        }
        // 큐 생성
        Deque<Integer> queue = new ArrayDeque<>();
        // 자료구조의 형태가 큐라면,
        for (int i = 0; i < N; i++) {
            if (listQueuestack[i] == 0) {
                queue.addFirst(currentList[i]); // 새로 만든 큐에 현재 요소를 담는다.
            }
        }
        for (int i = 0; i < M; i++) {
            queue.add(insertList[i]);
            answer.append((queue.pollFirst() + " "));
        }

        System.out.println(answer);
        reader.close();
    }
}