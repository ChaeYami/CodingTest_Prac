'''
완주하지 못한 선수
https://school.programmers.co.kr/learn/courses/30/lessons/42576
'''

def solution(participant, completion):
    answer = ''
        
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    if len(answer) == 0:
        answer = participant[-1]
    return answer