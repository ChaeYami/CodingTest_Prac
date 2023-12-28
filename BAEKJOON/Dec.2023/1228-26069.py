# https://www.acmicpc.net/problem/26069

import sys
input = sys.stdin.readline

N = int(input())
dancing = set()
dancing.add('ChongChong')

for _ in range(N):
     meet_lst = list(map(str, input().split()))
     for rabbit in meet_lst:
         if rabbit in dancing:
            meet_lst.remove(rabbit)
            dancing.add(meet_lst[0])
            
print(len(dancing))