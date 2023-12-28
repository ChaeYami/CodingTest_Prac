# 하샤드 수
'''
import os
os.system("cls")

# 리팩토링코드 - 리스트컴프리헨션 + 삼항연산자 + 변수 직관적으로 변경
def solution(x):
    # 리스트컴프리헨션
    sum_x = sum(int(x_) for x_ in str(x)) # 다수의 arg의 합! sum()은 다수의 arg를 가질 수 있으므로 가능! 
    answer = True if x % sum_x == 0 else False #삼항연산자
    return answer
'''
'''
# 리팩토링 - 코루틴적용 + 리스트컴프리헨션 + 삼항연산자
def solution():
    while True:
        x = yield
        # 리스트컴프리헨션
        y = sum([int(x_) for x_ in str(x)]) # list각 원소의 합!
        y = sum(int(x_) for x_ in str(x)) # 다수의 arg의 합! sum()은 다수의 arg를 가질 수 있으므로 가능! 
        answer = True if x % y == 0 else False #삼항연산자
        print(answer)

#코루틴 객체 생성
coco = solution()
#객체 실행 준비
next(coco)

#값 줘
coco.send(10)
coco.send(11)
coco.send(12)
coco.send(13)
coco.send(14)
coco.send(15)
'''

'''
인상적인 코드
def solution(n):
    return n%sum(int(x) for x in str(n)) == 0
'''

'''
def solution(x):
    # 하샤드수 판별!
    # X가 양의정수! 각 자리수를 더해야한다 → 반복! 반복문! for 사용!
    # 자릿수별로 뽑아내야하니, 숫자형을 문자열로 변경 후 뽑아내자!
    str_x = str(x)
    y=0
    for i in str_x:
        y += int(i) 
    # 기존 x가 합한 수 y로 나누어 떨어지는지 판별
    if x % y == 0:
        answer = True
    return answer

x = 10
print(solution(x))
'''

def solution(x):
    answer = True
    seat = sum(map(int, list(str(x))))
    if x % seat:
        answer = False
    return answer


print(solution(10))
print(solution(12))
print(solution(11))
