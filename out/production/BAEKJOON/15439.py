# https://www.acmicpc.net/problem/15439

from itertools import permutations

N = int(input())
comb_count = len(list(permutations(range(1, N+1), 2)))
print(comb_count)