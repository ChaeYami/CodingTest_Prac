import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))
M = int(input())
list_C = list(map(int, input().split()))

## 스택은 무시하고 큐만 deque에 추가하기
queue = deque([])
for i in range(N):
    if list_A[i] == 0:
        queue.appendleft(list_B[i])
    else:
        if queue == []:
            print(*list_C)
            sys.exit()

## deque가 하나의 큐 처럼 작동
for i in range(M):
    queue.append(list_C[i])
    print(queue.popleft(), end = " ")