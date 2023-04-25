# 0425 홀짝에 따라 다른 값 반환하기

def solution(n):
    answer = 0
    # 홀수의 경우와 짝수의 경우를 나눈다!
    # 홀/짝 판별은?
    if n%2 == 0: # 짝수라면,
        # for i in range(2, n+1, 2): # 더할 수들의 범위
        #     i = i**2 # 제곱했다!
        
        # 리스트컴프리헨션 사용
        answer = sum([i**2 for i in range(2, n+1, 2)])
            
    else: # 홀수라면,
        answer = sum(range(1, n+1, 2)) # 더할 수의 범위

    return answer

# 예시 출력해보기

print(solution(7)) # 예상출력값 16
print(solution(10)) # 예상출력값 220

# https://wikidocs.net/7023

'''
for i in range(10)
print(i)
0 1 2 3 4 5 6 7 8 9

ex n : 10 
2^2 + 4^2 + 6^2 + 8^2 + 10^2

1. 범위를 잡는다.
2. for 문을 돌린다.
3. 더한다!

'''

# ฅ(＾・ω・＾ฅ)