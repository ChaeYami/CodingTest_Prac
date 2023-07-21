# https://school.programmers.co.kr/learn/courses/30/lessons/181187

'''
x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인 서로 다른 크기의 원이 두 개 주어집니다. 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때, 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를 return하도록 solution 함수를 완성해주세요.
※ 각 원 위의 점도 포함하여 셉니다.
'''

'''
1사분면에서 

x축 위 : r1,0 ... r2,0
y축 위 : 0, r1 ... 0,r2
x = sqrt(r^2 - y^2)
y = sqrt(r^2 - x^2)
x좌표=y좌표일 때 (a,a) 라고 하면 a = sqrt(r^2 / 2)

1. x < r1
x = n 인 경우
y 의 최대 = sqrt(r2^2 - n^2)
y 의 최소 = sqrt(r1^2 - n^2)

2.r1 <= x < r2
x = n 인 경우
y 의 최대 = sqrt(r2^2 - n^2)
y 의 최소 = 0

x,y 축에 걸린 거 한번씩 빼주기
r1~r2 개수 *4
'''

from math import ceil, sqrt


def solution(r1, r2):
    answer = 0
    answer1 = 0
    answer2 = 0
    for n in range(0,r1): # x < r1
        # y좌표가 소수일 경우 r2는 안쪽 정수로, r1는 바깥쪽 정수로 해줘야 함
        answer1  += int(sqrt(r2**2 - n**2)) - ceil(sqrt(r1**2 - n**2)) +1
    for n in range(r1, r2+1): # r1 <= x < r2
        answer2 += int(sqrt(r2**2 - n**2)) +1        
    answer = answer1 + answer2 
    answer = answer*4 - (r2-r1 +1)*4
    return answer

print(solution(2,3))