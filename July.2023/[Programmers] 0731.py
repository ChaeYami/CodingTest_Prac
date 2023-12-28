# https://school.programmers.co.kr/learn/courses/30/lessons/147355

'''
t1 에서 길이가 len(p1) 인 문자열 다 구하기
만약 len(t1) = 7 이고 len(p1) = 3 이라면
t1[0:3]
t1[1:4]
t1[4:]
이므로

t[0:len(p)]
부터
t[len(t)-len(p):]
까지가 만들수 있는 문자열임

'''

def solution(t, p):
    answer = 0
    len_t = len(t)
    len_p = len(p)
    for i in range (len_t-len_p + 1):
        slice_one=t[i:i+len_p]
        if int(slice_one) <= int(p):
            answer+=1
    return answer


t1 = "3141592"
p1 = "271"
# result 2
		
t2 = "500220839878"
p2 = "7"
# result 8

t3 = "10203"
p3 = "15"
# result 3

solution(t1,p1)
solution(t2,p2)
solution(t3,p3)


'''
다른 사람 풀이

def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer
'''