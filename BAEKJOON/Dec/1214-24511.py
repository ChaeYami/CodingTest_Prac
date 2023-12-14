import sys
from collections import deque


N = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))
list_b = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
list_c = list(map(int, sys.stdin.readline().split()))

deq = deque()

for i in range(N):
    if list_a == 0:
        