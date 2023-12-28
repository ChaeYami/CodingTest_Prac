# https://www.acmicpc.net/submit/20920

from collections import deque, Counter
import sys

input = sys.stdin.readline
lst = list(map(int, input().split(' ')))
word_cnt = lst[0]
voca_length = lst[1]

voca_lst = []

# 길이 조건 맞는 단어 모으기
for _ in range(word_cnt):
    word = input().rstrip()
    if len(word) >= voca_length:
        voca_lst.append(word)
        
# 빈도수 내림차순, 길이 내림차순, 단어 오름차순
voca = sorted(Counter(voca_lst).items(), key=lambda x: (-x[1], -len(x[0]), x[0])) 

for word,count in voca:
    print(word)