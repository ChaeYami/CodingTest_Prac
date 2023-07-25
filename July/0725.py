# https://school.programmers.co.kr/learn/courses/30/lessons/161989

'''
- 전체 벽의 길이 n / 롤러의 길이 m 
- 입출력 예에서 n = 9 , m = 4 , section = [2,3,6]
1. 2에서 한번 칠하면 2,3,4,5 칠해진다.
2. deque 이용하기 - section 리스트를 deque로 변환
2-2. 하나씩 빼면서 전부 없어질 때 까지 반복
3. 왼쪽에서 하나씩 빼기 위해 popleft() 사용
''' 


from collections import deque

def solution(n, m , section):
    
    answer = 0					
    paint = deque(section)
    
    while paint:
        start = paint.popleft()
        while paint and start + m > paint[0]: 
            paint.popleft()
        answer += 1
    
    return answer


n1 = 8
m1 = 4
section1 = [2, 3, 6] # 2

n2 = 5
m2 = 4
section2 = [1, 3] # 1

n3 = 4
m3 = 1
section3 = [1, 2, 3, 4] # 4

print(solution(n1, m1, section1)) # 2
print(solution(n2, m2, section2)) # 1 
print(solution(n3, m3, section3)) # 4