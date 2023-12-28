# https://www.acmicpc.net/problem/15650

from itertools import combinations
import sys

input = sys.stdin.readline
lst = list(map(int, input().split()))
N = lst[0]
M = lst[1]

numbers = list(range(1, N + 1))
combinations_list = list(combinations(numbers, M)) # 조합

for pair in [' '.join(map(str, combi)) for combi in combinations_list]:
    print (pair)