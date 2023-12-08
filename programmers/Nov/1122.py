def solution(v):    
    answer = []

    if v[0][0] == v[1][0]:
        answer.append(v[2][0])
    else:
        answer.append(v[1][0])

    if v[0][1] == v[1][1]:
        answer.append(v[2][1])
    else:
        answer.append(v[1][1])


    return answer

print(solution([[1,4],[3,4],[3,10]]))

