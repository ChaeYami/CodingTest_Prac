# https://www.acmicpc.net/problem/15649

from itertools import permutations
import sys

input = sys.stdin.readline
lst = list(map(int, input().split()))
N = lst[0]
M = lst[1]

numbers = list(range(1, N + 1))
permutations_list = list(permutations(numbers, M)) # 순열

for pair in [' '.join(map(str, permutations)) for permutations in permutations_list]:
    print (pair)