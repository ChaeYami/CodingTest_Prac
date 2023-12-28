# https://www.acmicpc.net/problem/1010

import math
# from itertools import combinations
#
# N = int(input())
# for _ in range(N):
#     answer = 0
#     w, e = map(int, input().split())

#     east_sites = list(range(1,e+1))

#     sites = list(combinations(east_sites, w))

#     answer = len(sites)

#     print(answer)

N = int(input())

for _ in range(N):
    w, e = map(int, input().split())
    bridge = math.factorial(e) // (math.factorial(w) * math.factorial(e - w))
    print(bridge)