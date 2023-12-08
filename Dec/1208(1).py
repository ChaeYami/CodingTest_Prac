
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

# 1 번 풀이

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for i in permutations(dungeons, len(dungeons)):
        count = 0
        left_k = k 
        for min_need, need_k in i:
            
            if left_k >= min_need:
                left_k -= need_k
                count += 1
                
        if answer < count:
            answer = count
            
    return answer


# 2번 풀이

answer = 0
def DFS(k, complete, dungeons, check):
    global answer
    answer = max(answer, complete) # 탐험 수가 크면 업데이트
    for i in range(len(dungeons)):
        
	    # 방문하지 않은 던전이고, 최소 피로도보다 크면
        if check[i] == 0 and k >= dungeons[i][0]:
	        # 방문처리
            check[i] = 1
            
            DFS(k-dungeons[i][1], complete+1, dungeons, check)
            check[i] = 0

def solution(k, dungeons):
    global answer
    
    check = [0]*len(dungeons) # 방문 여부
    DFS(k, 0, dungeons, check) # 0: 방문한 던전의 개수를 0으로
    
    return answer