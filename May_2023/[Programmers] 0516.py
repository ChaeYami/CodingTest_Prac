#대문자와 소문자
def solution(my_string):
    answer = ''
    #for문을 통해 문자열 빼기
    for i in my_string:
        #만약 i가 소문자라면 대문자로
        if i.islower() == True:
            answer += i.upper()
        else:
            answer += i.lower()
    return answer
#이준영님의 풀이 1
def solution(my_string):
    answer = ''
    for i in my_string:
        if ord(i) >= 97:
            answer += chr(ord(i) - 32)
        else:
            answer += chr(ord(i) + 32)
    return answer
#이준영님의 풀이 2
def solution(my_string):
    #swapcase()는 대소문자를 바꿔주는 함수
    return my_string.swapcase()
print(solution("cccCCC")) #CCCCCC
print(solution("abCdEfghIJ")) #ABcDeFGHij
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
# 문자열의 중복값
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer

#인덱스바꾸기
def solution(my_string, num1, num2):
    answer = ''
    list_a = []
    for i in my_string:
        list_a.append(i)
    list_a[num1],list_a[num2] = list_a[num2],list_a[num1]
    answer = ''.join(list_a)
    return answer
#인덱스바꾸기 준영님풀이
def solution(my_string, num1, num2):
    answer = ''
    my_list = list(my_string)
    character1 = my_list[num1]
    character2 = my_list[num2]
    my_list[num1] = character2
    my_list[num2] = character1
    for a in my_list:
        answer += a
    return answer
print(solution("hello",1,2)) #hlelo
print(solution("I love you",3,6)) #l l veoyou