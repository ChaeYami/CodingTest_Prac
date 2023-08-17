def solution(bin1, bin2):
    answer = ''

# 2진수 > 10진수로 변환 > 더하기 > 2진수 변환
    bin1_ten = int(bin1,2)
    bin2_ten = int(bin2,2)
    bin_sum = bin1_ten + bin2_ten

    # 다시 2진수로 변환! --> bin() 함수 사용 : 0b+2진수 형태로 출력됨
    binary = bin(bin_sum)[2:]
    answer = binary

    return answer
'''
bin 함수 : 2진수를 넣으면 10진수로 출력해주는 함수
ex)>>> bin(42)
'0b101010'
'''
# 반환값은 모두 문자열
# format(100, '#b') = 0b1100100
# format(100, 'b') = 1100100 


# #주사위게임2
# def solution(a, b, c):
#     A = int(a)
#     B = int(b)
#     C = int(c)

#     #3개의 값이 다를 경우
#     if A != B != C:
#         return (A+B+C)
#     #3개의 값이 같을 경우
#     elif A == B == C:
#         return (A+B+C)*((A**2)+(B**2)+(C**2))*((A**3)+(B**3)+(C**3))
#     #2개의 값이 같을 경우
#     else:
#         return (A+B+C)*((A**2)+(B**2)+(C**2))
    


# print(solution(2,6,1)) #결과값9
# print(solution(5,3,3)) #결과값473
# print(solution(4,4,4)) #결과값110592