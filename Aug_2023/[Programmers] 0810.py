# https://school.programmers.co.kr/learn/courses/30/lessons/133499

'''
머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
'''

'''
옹알이(1) 에서 풀었던 것
def solution(babbling):
    answer = 0
    check = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in check:
            i = i.replace(j, " ", 1)  # babbling에서 주어진 단어를 공백처리
        if i.isspace():  # 공백으로 이루어진 단어를 count    i.isspace() -> True
            answer += 1
    return answer
    
에서 연속하는 발음 제거
'''

def solution(babbling):
    answer = 0
    check = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in check:
            if j * 2 not in i:
                i = i.replace(j, " ")  # babbling에서 주어진 단어를 공백처리
        if i.isspace():  # 공백으로 이루어진 단어를 count    i.isspace() -> True
            answer += 1
    return answer