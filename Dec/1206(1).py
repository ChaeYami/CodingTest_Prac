import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 리스트를 힙으로 바로 만들어줌
    
    while scoville[0] < K: # 원하는 스코빌 지수가 될 때 까지
        if len(scoville)>1:
            answer += 1
            # first = heapq.heappop(scoville) 
            # second = heapq.heappop(scoville) 
            # heapq.heappush(scoville, first + second *2)
            new_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            heapq.heappush(scoville, new_scoville)
        else:
            return -1
    return answer