#머쓱이보다 키큰사람
def solution(array, height):
    answer = 0
    #배열의 한명씩 뽑는다
    for i in array:
        #만약 그  i중 주어진 키보다 크다면 answer+1
        if height < i:
            answer+=1
    return answer
print(solution([149, 180, 192, 170],167)) #3
print(solution([180, 120, 140],190)) #0

def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    answer = array.index(height)
    return answer