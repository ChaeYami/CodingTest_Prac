'''
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
'''


def solution(phone_number):
    #입력값: 문자열이 들어와서 → 리턴값: 문자열로 출력되어야 한다.
    #<1> 마지막 뒷 4자리를 빼고,
    #<2> 가려야한다. == "*"로 바꿔준다.
    #<3> 출력한다.

    slicing = phone_number[:-4] #<1>
    answer = phone_number.replace(slicing,'*'*len(slicing)) #<2>
    return answer #<3>

# 01033334444 → *******4444

phone_number = "01033334444"  #기대결과 "*******4444"

print(solution(phone_number)) # 결과 "*******4444"