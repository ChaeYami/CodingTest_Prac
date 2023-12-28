import math
import time

"""
두 문자열 s와 skip, 자연수 index

문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줍니다.
index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아갑니다.
skip에 있는 알파벳은 제외하고 건너뜁니다.

제한사항
5 ≤ s의 길이 ≤ 50
1 ≤ skip의 길이 ≤ 10
s와 skip은 알파벳 소문자로만 이루어져 있습니다.
skip에 포함되는 알파벳은 s에 포함되지 않습니다.
1 ≤ index ≤ 20

"""

def solution1(s, skip, index):
    answer = ''
    # 모든 알파벳
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # z를 넘어가면 다시 a부터 시작
    # 문자열 s의 각 알파벳을 index 만큼 뒤의 알파벳으로
    # s가 문자열이고, alphabet 문자열도 정의해줬으니까 인덱스를 사용해볼까?
    # s문자열을 하나씩 돌면서 알파벳을 바꿔주거나 skip 하거나! 냐옹
    
    # skip에 있는 애들 먼저 없애버리기!
    for i in skip:
        alphabet = alphabet.replace(i,"" ) 
            
    # 문자열 바꿔주는 작업 하기!
    for j in s:
        # 알파벳을 바꿔주기 -> 인덱스를 먼저 찾기
        new_j = alphabet[(alphabet.index(j)+index)%len(alphabet)]
        answer += new_j
    return answer

def solution2(s, skip, index):
    answer = ''
    # 모든 알파벳
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz' # z를 넘어가면 다시 a부터 시작
    # 문자열 s의 각 알파벳을 index 만큼 뒤의 알파벳으로
    # s가 문자열이고, alphabet 문자열도 정의해줬으니까 인덱스를 사용해볼까?
    # s문자열을 하나씩 돌면서 알파벳을 바꿔주거나 skip 하거나! 냐옹
    n = 1
    # skip에 있는 애들 먼저 없애버리기!
    for i in skip:
        alphabet = alphabet.replace(i,"" ) 
            
    # 문자열 바꿔주는 작업 하기!
    for j in s:
        # 알파벳을 바꿔주기 -> 인덱스를 먼저 찾기
        new_j = alphabet[(alphabet.index(j)+index)%len(alphabet)]
        answer += new_j
    return answer

# 아스키 코드 변환 함수 사용
def solution3(s, skip, index):
    result = ''
    for char in s:
        if char in skip:  # skip에 포함된 문자는 건너뜁니다.
            continue
        new_char = chr((ord(char) - ord('a') + index) % 26 + ord('a'))  # 문자를 index만큼 뒤로 이동시킵니다.
        result += new_char
    return result



# 입출력 예\
    
start_time = time.perf_counter() # 시작 시간 저장

# 코드 실행
answer = solution1("aukks", "wbqd", 5)

end_time = time.perf_counter() # 종료 시간 저장

print(answer, "실행 시간:", round((end_time - start_time), 9)) # 소요된 시간 출력



start_time = time.perf_counter() # 시작 시간 저장

# 코드 실행
answer = solution2("aukks", "wbqd", 5)

end_time = time.perf_counter() # 종료 시간 저장

print(answer, "실행 시간:", round((end_time - start_time), 9)) # 소요된 시간 출력


start_time = time.perf_counter() # 시작 시간 저장

# 코드 실행
answer = solution3("aukks", "wbqd", 5)

end_time = time.perf_counter() # 종료 시간 저장

print(answer, "실행 시간:", round((end_time - start_time), 9)) # 소요된 시간 출력

