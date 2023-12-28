# https://www.acmicpc.net/problem/2164
from collections import deque

import sys
input = sys.stdin.readline

N = int(input())

deq = deque(range(1, N + 1))

while len(deq) > 1:
    deq.popleft()
    top = deq.popleft()
    deq.append(top)
    
print(deq[0])