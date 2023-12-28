# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        tem = arr[i]
        if i == 0:
            answer.append(tem)
        else:
            if tem != arr[i-1]:
                answer.append(tem)
        
    return answer
