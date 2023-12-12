# https://www.acmicpc.net/problem/11866

from collections import deque

n, k = map(int, input().split())
deq = deque(list(range(1, n+1)))

answer = []
a = 0
while deq:
    now_turn = deq.popleft()
    a += 1  
    if a == k:
        answer.append(str(now_turn)) # join을 위해 str으로 바꿔서 넣어줌
        a = 0
    else: 
        deq.append(now_turn)
print('<'+', '.join(answer)+'>')


'''
리스트에서 앞에서 하나씩 빼서 뒤에 붙이는 형식으로 원의 형태를 유지한다.
세번째 행동일 때 리스트에서 삭제하고 stack에 넣어 빠진 사람을 저장
반복해서 리스트가 비면 모든 사람이 제거된 것이므로 종료
'''