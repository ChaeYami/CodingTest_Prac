# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    # citations 요소 중 하나(citation)
    # [3,0,6,1,5]
    # [0,1,3,5,6]
    # citations[i] > i+1 --> i
    # 3도 되고 1도 되넹
    # 최댓값이면 걍 내림차순으로 정렬해서?
    # [6,5,3,1,0]
    # citations[i] < i+1 일 때 i   
    
    # [10, 11] H-Index = 2
    # [10, 10, 10]
    
    sorted_citation = sorted(citations,reverse = True)
    for i in range(len(citations)):
        if sorted_citation[i] < i+1:
            answer = i
            return answer

    answer = len(citations)
    return answer

