# 콜라츠 추측
# 페어프로그래밍 코드
def solution(num):
    # 주어진 수 num이 1 일 때 와 짝수 일 때, 홀수 일 때로 분리
    answer = 0
    # num이 1 일 때
    while num > 1:
        # num이 짝수 일 때
        if num%2 == 0:
            num = num/2
        # num이 홀수 일 때
        else:
            num = num*3 + 1
        answer += 1
        
        if answer > 500:
            answer = -1
            break
    return answer
        
# 리팩토링 코드
def solution(num):
    # 주어진 수 num이 1 일 때 와 짝수 일 때, 홀수 일 때로 분리
    answer = 0
    # num이 1 일 때
    while num > 1:
        # 삼항연산자 사용
        num = num/2 if num%2 == 0 else num*3 + 1   
        answer += 1
        
        if answer > 500:
            answer = -1
            break
        else:
            answer = answer
    return answer
    
    
# 흠터레스팅
def collatz(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1

print(solution(6))    
print(solution(16))    
print(solution(626331))   


# 6	8
# 16	4
# 626331	-1
