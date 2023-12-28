# https://www.acmicpc.net/problem/15651

from itertools import product
import sys

input = sys.stdin.readline
lst = list(map(int, input().split()))
N = lst[0]
M = lst[1]

numbers = list(range(1, N + 1))
products_list = list(product(numbers, repeat = M)) # 중복순열

for pair in [' '.join(map(str, pro)) for pro in products_list]:
    print (pair)