
from itertools import combinations

n, r = map(int, input().split())
arr = list(range(n))

print(len(list(combinations(arr, r))))