#두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 
#주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

# 풀이 1 : for문 사용하기
def solution(s1, s2):
    answer = 0
    for s in s1: # s1의 요소를 하나씩 돌아간다
        for sc in s2:
            if s == sc:
                answer+=1
    return answer

# 1-1 리팩토링
def solution(s1, s2):
    answer = 0
    for s in s1: # s1의 요소를 하나씩 돌아간다
        if s in s2: # if 에서 in : 요소가 있다면 True #대박대박
            answer += 1 
    return answer
       
# 풀이 2 : 집합으로 풀기!
# set 형 - 중복을 허용하지 않는 자료형
'''
set1, set2

교집합 & : set1&set2 / set1.intersection(set2)
합집합 | : set1|set2
차집합 - : set1-set2
'''
def solution(s1, s2):
    answer = len(set(s1) & set(s2))
    return answer


s1 = ["a", "b", "c"] 
s2 = ["com", "b", "d", "p", "c"]

print(solution(s1,s2)) # 2

s3 = ["n", "omg"]
s4 = ["m", "dot"]
print(solution(s3,s4)) # 0
