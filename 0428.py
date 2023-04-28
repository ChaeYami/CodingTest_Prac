def solution(num, total):
    answer = []
    first = (total - num*(num-1)//2)//num
    final = first + num -1
    answer = [i for i in range(first, final+1)]
    return answer

    # average = total/num
    # first = 
    # final = first + num -1
    # average = (first + final)/2
    # average * num = total
    # (first + first + num -1)/2 * num  = total = num*first+num*(num-1)/2

    '''
    3개 더해서 12!
    12/3 = 4 
    3 + 4 + 5
    1,2,3,4,5,6
    2,3,4,5,6
    5개 더해서 15!
    15/5 = 3
    1 + 2 + 3 + 4 + 5 =15
    total / num = a
    
    갯수 num 더한결과 total
    시작값 n 마지막값 n + (num-1) 

    n + n+1 + n+2 + ... + n+(num-1) = total
    첫째항이 n이고 마지막항이 n + (num-1) 갯수가 num인 수열
    total = (num(n+n+num-1)) / 2 등차수열의 합!
    
    
    n = 1
    total = n
    list = [n]
    
    '''
# 다른 사람 풀이
def solution(num, total):
    if num % 2 == 1:
        return list(range(total//num-num//2, total//num+num//2+1))
    else:
        return list(range(total//num-num//2+1, total//num+num//2+1))

    # 입출력 예
print(solution(3, 12)) # [3, 4, 5]
print(solution(5, 15)) # [1, 2, 3, 4, 5]
print(solution(4, 14)) # [2, 3, 4, 5]
print(solution(5, 5) )# [-1, 0, 1, 2, 3]