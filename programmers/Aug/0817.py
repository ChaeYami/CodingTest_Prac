# https://school.programmers.co.kr/learn/courses/30/lessons/176962?language=python3

'''
과제를 받은 루는 다음과 같은 순서대로 과제를 하려고 계획을 세웠습니다.

- 과제는 시작하기로 한 시각이 되면 시작합니다.
- 새로운 과제를 시작할 시각이 되었을 때, 기존에 진행 중이던 과제가 있다면 진행 중이던 과제를 멈추고 새로운 과제를 시작합니다.
- 진행중이던 과제를 끝냈을 때, 잠시 멈춘 과제가 있다면, 멈춰둔 과제를 이어서 진행합니다.
    - 만약, 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면, 새로 시작해야 하는 과제부터 진행합니다.
- 멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작합니다.

과제 계획을 담은 이차원 문자열 배열 plans가 매개변수로 주어질 때, 과제를 끝낸 순서대로 이름을 배열에 담아 return 하는 solution 함수를 완성해주세요.
'''

'''
라운드 로빈 스케쥴링 방식을 코드로 구현하라는 느낌

'''

def solution(plans):
    answer = []
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]),int(x[2])],plans), key=lambda x:-x[1])
    lst = []
    while plans :
        x = plans.pop()
        for i,v in enumerate(lst):
            if v[0]>x[1]:
                lst[i][0] +=x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()
    answer =  list(map(lambda x: x[1], lst))
    return answer


plans1 = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
plans2 = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
plans3 = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]

print(solution(plans1)) # ["korean", "english", "math"]
print(solution(plans2)) # ["science", "history", "computer", "music"]
print(solution(plans3)) # ["bbb", "ccc", "aaa"]