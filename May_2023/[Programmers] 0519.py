'''
첫시도
def solution(babbling):
    answer = 0
    check = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in check:
            i = i.replace(j, "", 1)  # babbling에서 주어진 단어를 삭제
        if len(i) == 0:  # 문자열이 남지 않은 요소만 count    
            answer += 1
    return answer
'''

def solution(babbling):
    answer = 0
    check = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in check:
            i = i.replace(j, " ", 1)  # babbling에서 주어진 단어를 공백처리
        if i.isspace():  # 공백으로 이루어진 단어를 count    i.isspace() -> True
            answer += 1
    return answer

