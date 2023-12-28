# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    for i in range(len(s)):
        find_one = s[:i].rfind(s[i])
        if find_one >= 0:
            answer.append(len(s[:i]) - find_one)
        else:
            answer.append(find_one)
    return answer

s1 = "banana" # [-1, -1, -1, 2, 2, 2]
s2 = "foobar" # [-1, -1, 1, -1, -1, -1]

solution(s1)
solution(s2)
