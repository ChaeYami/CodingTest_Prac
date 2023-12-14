import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main{
        static StringBuilder answer = new StringBuilder();
        static Deque<Integer> deque = new ArrayDeque<>();

        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st;

            int N = Integer.parseInt(br.readLine());

            while(N-- > 0){
                st = new StringTokenizer(br.readLine());
                int tkr = Integer.parseInt(st.nextToken());

                switch (tkr) {
                    case 1:
                        deque.addFirst(Integer.parseInt(st.nextToken()));
                        break;
                    case 2:
                        deque.addLast(Integer.parseInt(st.nextToken()));
                        break;
                    case 3:
                        answer.append(deque.isEmpty() ? -1 : deque.pollFirst()).append("\n");
                        break;
                    case 4:
                        answer.append(deque.isEmpty() ? -1 : deque.pollLast()).append("\n");
                        break;
                    case 5:
                        answer.append(deque.size()).append("\n");
                        break;
                    case 6:
                        answer.append(deque.isEmpty() ? 1 : 0).append("\n");
                        break;
                    case 7:
                        answer.append(deque.isEmpty() ? -1 : deque.peekFirst()).append("\n");
                        break;
                    case 8:
                        answer.append(deque.isEmpty() ? -1 : deque.peekLast()).append("\n");
                        break;
                }
            }
            br.close();
            System.out.println(answer);
        }
}